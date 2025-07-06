# 🏫 Dimraj AiCampus (DAIC)

> 🚀 Institutional Intelligence Suite for Education & Enterprise – Powered by FastAPI, OpenAI, and LangChain

Dimraj AiCampus (DAIC) is a modern AI backend designed to serve the **entire education ecosystem** – from schools and colleges to coaching centers and education enterprises.

Built by [Dimraj Technologies](https://dimraj.com), DAIC empowers institutions to automate, analyze, and enhance every academic and administrative process.

---

## 📦 Project Structure

dimraj-aicampus/
│
├── app/
│ └── main.py # Backend code with all endpoints
├── requirements.txt # Required Python packages
├── .env.example # Sample API key format
├── README.md # You're reading it
└── .gitignore # Ignore virtual envs, .env, etc.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/MUKULGOYL/dimraj-aicampus.git
cd dimraj-aicampus
python -m venv venv
pip install -r requirements.txt
OPENAI_API_KEY=your-real-openai-key
uvicorn app.main:app --reload
| Endpoint                  | Function                       |
| ------------------------- | ------------------------------ |
| `POST /generate-lesson`   | Create AI-powered lesson plans |
| `POST /generate-quiz`     | Auto-generate quizzes          |
| `POST /solve-doubt`       | Answer student doubts          |
| `POST /explain-concept`   | Simple concept explanations    |
| `POST /summarize-report`  | Summarize admin reports        |
| `POST /parent-message`    | Message generator for parents  |
| `POST /syllabus-planner`  | Plan syllabus week-by-week     |
| `POST /generate-homework` | AI homework assignment creator |
| `POST /student-analysis`  | Analyze student performance    |
| `GET /erp`                | ERP features overview          |
🙌 Built by Dimraj Technologies
Leading India's AI transformation in education, business, and beyond.

🌐 dimrajtechnologies.com | 📩 dimrajtechnologies@gmail.com | 🧠 LinkedIn:- http://linkedin.com/company/dimrajtechnologies
