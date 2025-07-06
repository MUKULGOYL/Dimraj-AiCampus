# 📘 Dimraj AiCampus (DAIC) – Institutional Intelligence Suite
# Full Backend Code (FastAPI + LangChain + OpenAI)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

# 🔑 Load environment variables
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🧠 Initialize LLM
llm = OpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)

# Prompt Templates
lesson_plan_prompt = PromptTemplate(
    input_variables=["topic", "grade"],
    template="""
    You are an expert school educator. Generate a detailed lesson plan for the topic \"{topic}\" for Grade {grade}. 
    Include: learning objectives, materials needed, activities, real-life examples, and short quiz questions.
    """
)
lesson_chain = LLMChain(llm=llm, prompt=lesson_plan_prompt)

quiz_prompt = PromptTemplate(
    input_variables=["topic", "grade"],
    template="""
    Generate a 5-question quiz on the topic \"{topic}\" for Grade {grade}. Include 4 options and the correct answer for each.
    """
)
quiz_chain = LLMChain(llm=llm, prompt=quiz_prompt)

explanation_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
    Explain this concept to a Grade 6 level learner in simple terms: \"{question}\".
    Include real-life examples and analogies for better understanding.
    """
)
explanation_chain = LLMChain(llm=llm, prompt=explanation_prompt)

solve_doubt_prompt = PromptTemplate(
    input_variables=["doubt", "grade"],
    template="""
    Act like a friendly educator. Solve this learner's doubt: \"{doubt}\" for a Grade {grade} level. 
    Make it clear, simple, and relatable.
    """
)
doubt_chain = LLMChain(llm=llm, prompt=solve_doubt_prompt)

report_summary_prompt = PromptTemplate(
    input_variables=["report_data"],
    template="""
    Summarize this institutional academic report data: \"{report_data}\".
    Provide insights in bullet points for school administrators.
    """
)
report_chain = LLMChain(llm=llm, prompt=report_summary_prompt)

parent_msg_prompt = PromptTemplate(
    input_variables=["context"],
    template="""
    Draft a professional message to be sent from a school to parents. Message context: \"{context}\".
    """
)
parent_msg_chain = LLMChain(llm=llm, prompt=parent_msg_prompt)

syllabus_planner_prompt = PromptTemplate(
    input_variables=["syllabus", "weeks"],
    template="""
    Break down the following syllabus into a weekly plan over {weeks} weeks:
    {syllabus}
    Provide bullet points for each week's content.
    """
)
syllabus_chain = LLMChain(llm=llm, prompt=syllabus_planner_prompt)

homework_prompt = PromptTemplate(
    input_variables=["topic", "grade"],
    template="""
    Generate a weekly homework assignment for the topic \"{topic}\" suitable for Grade {grade}. Include exercises, reading, and creative activities.
    """
)
homework_chain = LLMChain(llm=llm, prompt=homework_prompt)

student_analysis_prompt = PromptTemplate(
    input_variables=["performance_data"],
    template="""
    Analyze this student's performance data: \"{performance_data}\".
    Provide strengths, weaknesses, and improvement suggestions.
    """
)
analysis_chain = LLMChain(llm=llm, prompt=student_analysis_prompt)

# 📦 API Setup
app = FastAPI(title="Dimraj AiCampus (DAIC)", version="2.0")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧾 Input Schemas
class LessonInput(BaseModel):
    topic: str
    grade: str

class DoubtInput(BaseModel):
    doubt: str
    grade: str

class ExplanationInput(BaseModel):
    question: str

class ReportInput(BaseModel):
    report_data: str

class ParentMessageInput(BaseModel):
    context: str

class SyllabusPlannerInput(BaseModel):
    syllabus: str
    weeks: int

class HomeworkInput(BaseModel):
    topic: str
    grade: str

class StudentAnalysisInput(BaseModel):
    performance_data: str

# 📌 Routes
@app.get("/")
def root():
    return {"message": "Welcome to Dimraj AiCampus (DAIC) – Institutional Intelligence Services"}

@app.post("/generate-lesson")
def generate_lesson(data: LessonInput):
    try:
        result = lesson_chain.run(topic=data.topic, grade=data.grade)
        return {"lesson_plan": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-quiz")
def generate_quiz(data: LessonInput):
    try:
        result = quiz_chain.run(topic=data.topic, grade=data.grade)
        return {"quiz": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/solve-doubt")
def solve_doubt(data: DoubtInput):
    try:
        result = doubt_chain.run(doubt=data.doubt, grade=data.grade)
        return {"solution": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/explain-concept")
def explain_concept(data: ExplanationInput):
    try:
        result = explanation_chain.run(question=data.question)
        return {"explanation": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize-report")
def summarize_report(data: ReportInput):
    try:
        result = report_chain.run(report_data=data.report_data)
        return {"summary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/parent-message")
def parent_message(data: ParentMessageInput):
    try:
        result = parent_msg_chain.run(context=data.context)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/syllabus-planner")
def syllabus_planner(data: SyllabusPlannerInput):
    try:
        result = syllabus_chain.run(syllabus=data.syllabus, weeks=data.weeks)
        return {"weekly_plan": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-homework")
def generate_homework(data: HomeworkInput):
    try:
        result = homework_chain.run(topic=data.topic, grade=data.grade)
        return {"homework": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/student-analysis")
def student_analysis(data: StudentAnalysisInput):
    try:
        result = analysis_chain.run(performance_data=data.performance_data)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/erp")
def erp_overview():
    return {
        "erp": "ERP module loaded.",
        "features": [
            "AI-based attendance system",
            "Class schedule generation",
            "Payroll and HR tools",
            "Fee tracking and invoice generation",
            "Student record management",
            "Parent communication center",
            "Analytics dashboard for school admins"
        ]
    }

# ▶️ To run: uvicorn main:app --reload
