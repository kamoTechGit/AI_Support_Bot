# AI Support Bot

This project provides a hands-on introduction to AI and automation using:

* FastAPI (build an API)
* LLMs (AI responses)
* Docker (containerization)
* GitHub Actions (CI/CD)

By the end, you will understand how a simple AI-powered system is built, packaged, and automated.

---

# What You Will Build

A small API that:

* Accepts a question via `/ask`
* Uses a knowledge file (`knowledge.txt`)
* Sends context to an LLM
* Returns an AI-generated answer

---

# How It Works

User → API → LLM → Response
    ↘ knowledge.txt

We provide the AI with context and a question, and it generates an answer.

---

# Tech Stack

* FastAPI (Python API)
* LLM (OpenAI or Ollama)
* Docker
* GitHub Actions

---

# Project Structure

```
ai-support-bot/
│
├── app/
│   ├── main.py          # API entrypoint
│   ├── llm.py           # LLM logic
│   └── knowledge.txt    # Your data
│
├── Dockerfile
├── requirements.txt
└── .github/workflows/   # CI/CD pipeline
```

---

# Step-by-Step Guide

## 1. Run the API (no AI yet)

Start simple.

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Test:

```
POST http://localhost:8000/ask
{
  "question": "What are your office hours?"
}
```

At this stage, the response is mocked.

---

## 2. Add the AI (LLM)

Update `llm.py` to call a real model.

Options:

* OpenAI (cloud)
* Ollama (local models)

Goal:

* Send knowledge and question
* Get a generated answer

---

## 3. Improve the Prompt

Experiment:

* What happens if you change instructions?
* Can you force it to say “I don’t know”?
* Does it stay grounded in the knowledge file?

👉 This is where real learning happens.

---

## 4️ Dockerize the App

Build:

```bash
docker build -t ai-support-bot .
```

Run:

```bash
docker run -p 8000:8000 ai-support-bot
```

Now the app runs anywhere.

---

## 5️ Add CI/CD (Automation)

We use GitHub Actions to:

* Automatically build the Docker image
* Run on every push

Check:

```
.github/workflows/docker.yml
```

---

# Exercises (Important)

Try these before moving on:

### 🟢 Easy

* Add more data to `knowledge.txt`
* Ask better questions

### 🟡 Medium

* Add logging (print questions + answers)
* Handle unknown questions gracefully

### 🔴 Challenge

* Only answer using the knowledge file
* Reject unrelated questions

---

# ⚠️ Key Lessons

* LLMs are **not databases**
* Prompt design matters more than code
* Keep systems simple before scaling

---

#  Optional Extensions

If you want to go further:

* Add a frontend (simple HTML)
* Store past questions
* Add basic retrieval (mini-RAG)
* Deploy to the cloud

---

# Notes

* Don’t rush into complexity
* Let's break things
* Focus on understanding the flow:
  → input → prompt → model → output

---

# Goal

You should walk away understanding:

* How AI is actually integrated into apps
* How Docker makes apps portable
* How automation (CI/CD) fits into real workflows

---

Happy building !!!
