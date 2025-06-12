from fastapi import FastAPI, Request
from litellm import completion
import os
import json

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


@app.post("/generate")
async def generate(request: Request):
    try:
        # Get raw JSON body
        body = await request.json()
        prompt = body.get("prompt")

        if not prompt:
            return {"error": "Prompt is required"}

        # Call Groq API
        response = completion(
            model="groq/llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            api_key=GROQ_API_KEY
        )

        return {"response": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}