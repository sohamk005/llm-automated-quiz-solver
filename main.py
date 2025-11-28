# main.py
import os
from fastapi import FastAPI, HTTPException, BackgroundTasks, Request
from pydantic import BaseModel
from utils import run_quiz_process

app = FastAPI()

# Verify your environment variables are set
# os.environ["AIPROXY_TOKEN"] should be set in your deployment environment

class QuizRequest(BaseModel):
    email: str
    secret: str
    url: str

# Define your secret here (match this with what you put in Google Form)
MY_SECRET = "my_super_secure_secret_123" 

@app.post("/run")
async def run_quiz(request: QuizRequest, background_tasks: BackgroundTasks):
    # 1. Verify Secret
    if request.secret != MY_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # 2. Trigger the solver in the background
    # We pass the email and the starting URL
    print(f"Received task for {request.email} at {request.url}")
    background_tasks.add_task(run_quiz_process, request.email, request.secret, request.url)

    # 3. Respond immediately with 200 OK
    return {"message": "Task received and processing started"}

@app.get("/")
def read_root():
    return {"status": "Server is running"}