from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    message = os.getenv("APP_MESSAGE", "Hello FastAPI!")
    return {
        "app": "sample-fastapi",
        "message": message+' this is test-fast-api ok!'
    }
