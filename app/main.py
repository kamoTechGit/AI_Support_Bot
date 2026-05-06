from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import llm

load_dotenv()

app = FastAPI(title="AI Support Bot")

KNOWLEDGE_PATH = Path(__file__).parent / "knowledge.txt"


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    knowledge = KNOWLEDGE_PATH.read_text(encoding="utf-8")
    answer = llm.ask(question=request.question, knowledge=knowledge)
    return AnswerResponse(answer=answer)
