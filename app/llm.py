import os
import httpx
from openai import OpenAI

PROMPT_TEMPLATE = """\
You are a helpful support assistant. Only answer using the provided knowledge.
If the answer is not in the knowledge, say "I don't know."

Knowledge:
{knowledge}

Question: {question}
Answer:"""


def ask(question: str, knowledge: str) -> str:
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    prompt = PROMPT_TEMPLATE.format(knowledge=knowledge, question=question)

    if provider == "ollama":
        return _ask_ollama(prompt)
    return _ask_openai(prompt)


def _ask_openai(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def _ask_ollama(prompt: str) -> str:
    url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
    model = os.getenv("OLLAMA_MODEL", "llama3")
    response = httpx.post(
        url,
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=60.0,
    )
    response.raise_for_status()
    return response.json()["response"].strip()
