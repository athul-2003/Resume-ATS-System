# Resume ATS System 🤖

Welcome to the **Resume ATS System**, an AI-powered tool designed to help students, job seekers, and professionals optimize their resumes for Applicant Tracking Systems (ATS). This application allows users to upload their resume in PDF format, analyze its compatibility with job descriptions, and receive valuable feedback on improving the resume to boost the chances of getting noticed by recruiters.

With the power of **Google Gemini's generative AI**, the system provides detailed evaluations of your resume, helping you understand its strengths, weaknesses, and areas for improvement. Whether you're a student entering the job market or a job seeker looking to refine your resume, this tool will help you craft a standout application that aligns with industry standards.

## Features
- **Resume and Job Description Analysis**: Compare your resume with a job description and receive a professional evaluation, including alignment with the role, strengths, gaps, and suggestions for improvement.
- **General ATS Resume Analysis**: Get a score for your resume, along with feedback on its format, keyword usage, strengths, weaknesses, and recommendations for an ATS-friendly version.
- **AI-Powered Suggestions**: Leverage Google Gemini's generative AI model to analyze your resume and offer detailed, actionable feedback.
  
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/athul-2003/Resume-ATS-System.git
    cd Resume-ATS-System
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Google Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload a PDF resume and analyze the extracted text.



## File Structure
```
Resume-ATS-System/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not included in repo)
└── README.md            # Project documentation
```

## Dependencies

- PyPDF2
- Streamlit
- google-generativeai
- python-dotenv



## Example Workflow
1. Upload your resume in PDF format.
2. Choose between "Analyze Resume for Job Description" or "General ATS Resume Analysis."
3. For job description analysis, input the job description and analyze how well your resume matches.
4. For ATS-friendly suggestions, get actionable tips on how to optimize your resume for Applicant Tracking Systems (ATS).
5. View the detailed feedback and suggestions for improving your resume.



## Demo
[**Watch Demo Video**](https://github.com/user-attachments/assets/2de935e4-5037-4f82-b17d-7e646e734912)


## Disclaimer  
The resume analysis results provided by the Resume ATS System are based on AI-generated evaluations and suggestions. While the analysis aims to provide valuable insights, it should not be considered an exhaustive or definitive assessment. The results may vary depending on the quality and formatting of the uploaded resume and the provided job description. For accurate results, users are encouraged to review the suggestions manually and seek additional professional feedback.

## Future Enhancements  
- **Job Description Parsing:** Automatically extract and parse job descriptions from various sources.
- **Multiple Resume Formats:** Expand support to analyze resumes in various formats (e.g., Word, Google Docs).
- **Improved Resume Scoring:** Introduce a more granular scoring system based on different job roles.
- **AI Model Updates:** Incorporate new versions of Google Gemini or other AI models for better analysis and suggestions.
- **Resume Template Generator:** Provide users with customizable ATS-friendly resume templates.

## Contributing  
Contributions are welcome! Feel free to fork the repository and submit a pull request. For major changes, please open an issue to discuss your ideas first.



## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Google Gemini API](https://developers.google.com/gemini)
- [python-dotenv](https://pypi.org/project/python-dotenv/)


⭐️ Don't forget to give this repo a star if you found it helpful!
