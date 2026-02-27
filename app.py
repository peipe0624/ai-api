from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "AI server running"}

@app.post("/ask")
def ask(q: Question):
    return {"answer": f"あなたの質問『{q.question}』を受け取りました！"}