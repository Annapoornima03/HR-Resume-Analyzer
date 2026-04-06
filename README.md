# Enterprise AI Recruitment System

A sophisticated, AI-driven recruitment management platform designed to automate the end-to-end hiring process. From resume parsing to automated interview scheduling, this system streamlines HR workflows with precision and efficiency.

## Key Features

- **AI Resume Analysis**: Leverages LLMs (Llama-3.3-70b) to extract skills, experience, and education from PDF, DOCX, and images.
- **Smart Candidate Scoring**: Adjustable weighting system (Technical, Experience, Education, JD Fit) with automatic shortlisting and rejection.
- **Job Requisition Management**: Create, manage, and delete multiple job postings, each with its own specific requirements and candidate pool.
- **Communication Hub**: Smart bulk emailing for selected or rejected candidates with customizable templates and status tracking.
- **Interview Scheduler**: Comprehensive scheduling manager that handles meeting links, duration, modes, and automated calendar invitations.
- **End-to-End Workflow Automation**: Process a batch of resumes from upload to top-candidate interview invitation in a single click.
- **Analytics & Reporting**: Visual insights into candidate distribution, skill matching, and recruitment funnel performance.

## Technology Stack

- **Frontend**: Streamlit
- **Intelligence**: LLM (Groq / Llama-3), spaCy, RapidFuzz
- **Data Processing**: pandas, numpy, pdfplumber, easyocr
- **Communication**: smtplib (SMTP)
- **Visualization**: Plotly

## Setup & Installation

### Prerequisites
- Python 3.9+
- Groq API Key
- SMTP Credentials (e.g., Gmail App Password)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd VCodez_FinalProject-main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. **System Configuration**: 
    - Set your Company Name and HR details in the sidebar.
    - Connect your SMTP server for email functionality.
2. **Job Definition**: 
    - Create a Job Requisition and define the Job Description and Required Skills.
    - Adjust scoring weights in the "Scoring & Filters" section.
3. **Resume Upload**: 
    - Upload multiple resumes in the "Resume Upload" tab.
    - Click "Analyze All" to start the AI evaluation.
4. **Pipeline Management**: 
    - Review candidates in the "Candidate Pipeline".
    - Filter by status or score.
5. **Interview Scheduling**: 
    - Select a candidate in the "Interview Scheduler".
    - Set the time and meeting link to send a formal invitation.
6. **Automation**: 
    - Use the "Workflow Automation" tab to process hundreds of resumes instantly.

## License
MIT License

smtp pass: cfkn yszj njaw wytw
smtp id: infotechcorp21@gmail.com