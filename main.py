# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI home page!"}

@app.get("/hello")
async def hello():
    return {"message": "Hello, FastAPI world!"}