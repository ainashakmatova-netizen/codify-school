import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

with open("knowledge.txt", "r", encoding="utf-8") as f:
    KNOWLEDGE = f.read()


def ask_ai(question):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": f"""
Ты AI помощник школы Codify.

Отвечай только используя информацию ниже.

Если информации нет —
напиши что студент может обратиться к менеджеру.

Информация:

{KNOWLEDGE}
"""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content