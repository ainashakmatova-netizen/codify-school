from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai import ask_ai

app = FastAPI(title="Codify AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@app.get("/")
def home():
    return {
        "status": "online",
        "school": "Codify"
    }


@app.post("/chat")
def chat(data: ChatRequest):

    question = data.messages[-1].content

    answer = ask_ai(question)

    return {
        "answer": answer
    }