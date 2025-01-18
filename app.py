import os
import PyPDF2
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini API
key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to extract text from uploaded PDF
def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        if not text.strip():
            raise ValueError("The extracted text from the resume is empty. Please upload a different PDF.")
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

# Function to match resume with job description
def analyze_resume(job_description, resume_text):
    prompt_job_desc = f"""As an experienced Technical Human Resource Manager, provide a detailed professional evaluation of the candidate's resume : {resume_text} against the job description: {job_description}. 

    Please analyze:
                    1. Overall alignment with the role, on a scale of 1-10
                    2. Key strengths and qualifications that match
                    3. Notable gaps or areas for improvement
                    4. Specific recommendations for enhancing the resume
                    5. Final verdict on suitability for the role

                    Format the response with clear headings and professional language.

                    Also, only if the final verdict is positive (score >= 7), provide a brief roadmap for the candidate to prepare for the interview with sample questions and key points to highlight, else specify to make suggested changes and apply again.
                    """

    # Get response from the model
    response = model.generate_content(prompt_job_desc)
    return response.text

# Function to calculate resume score and suggestions using Google Gemini
def get_suggestions_from_gemini(resume_text):
    prompt = f"""As an ATS (Applicant Tracking System) expert, analyze the following resume: {resume_text}
                Provide:
                        1. Overall resume score (%)
                        2. Resume format and structure analysis
                        3. Specific keywords found
                        4. Overall strengths and weaknesses
                        5. Specific recommendations for improvement
                        
                        Start with the percentage match prominently displayed.
                        At the end, create a more cleaner and structured resume that is more likely to be selected by the ATS.
                        """

    # Get response from the model
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI Configuration
st.set_page_config(page_title="Resume ATS System", page_icon="📄", layout="wide")
st.title("📄 Resume ATS System 🤖")
st.markdown(
    """
    **Welcome to the Resume ATS System!**  
    Upload your resume, analyze its compatibility with job descriptions, or get ATS-friendly suggestions.  
    """,
    unsafe_allow_html=True,
)

# Sidebar Configuration
st.sidebar.header("📋 Options")
analysis_type = st.sidebar.radio(
    "Choose an action:", 
    options=["", "Analyze Resume for Job Description", "General ATS Resume Analysis"],
    help="Select what you want to do with your resume."
)


# File Upload
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF only)", 
    type=["pdf"], 
    help="Ensure your resume is a PDF file for accurate text extraction."
)

if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    # Handle errors in text extraction
    if resume_text.startswith("Error"):
        st.error(resume_text)
    else:
        st.success("Resume uploaded and processed successfully! Proceed with your selected action.")
        
        # Option 1: Analyze Resume for Job Description
        if analysis_type == "Analyze Resume for Job Description":
            job_description = st.text_area(
                "Enter the Job Description:", 
                placeholder="Paste the job description here...",
                help="The more detailed the job description, the better the analysis.",
                height=150,
            )
            if st.button("Analyze Resume"):
                if job_description:
                    with st.spinner("Analyzing your resume against the job description..."):
                        analysis = analyze_resume(job_description, resume_text)
                    st.subheader("🔍 Resume Analysis Results")
                    with st.expander("View Detailed Analysis"):
                        st.markdown(analysis)
                else:
                    st.warning("Please provide a job description before proceeding.")

        # Option 2: General ATS Resume Analysis
        elif analysis_type == "General ATS Resume Analysis":
            if st.button("Generate ATS-Friendly Suggestions"):
                with st.spinner("Generating suggestions for an ATS-friendly resume..."):
                    suggestions = get_suggestions_from_gemini(resume_text)
                st.subheader("💡 ATS Resume Suggestions")
                with st.expander("View Suggestions"):
                    st.markdown(suggestions)
                st.success("Suggestions generated successfully!")

# Footer with Modern Styling
st.markdown(
    """
    <style>
        footer {visibility: hidden;}
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px 0;
            color: #aaa;
            font-size: 14px;
        }
        .footer a {
            color: inherit;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
     <div class="footer">Built by 🎉 <a href="https://www.linkedin.com/in/h-athulkrishnan/">H Athulkrishnan</a> | <a href="https://github.com/athul-2003">Github</a>🚀</div>
    """,
    unsafe_allow_html=True,
)
