from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from detoxify import Detoxify

class messageText(BaseModel):
    text: str

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/checkText")
def checkText(postText: messageText):
    results = Detoxify('original').predict(postText.text)
    textOk = True
    for category in results:
        if results[category] > 0.4:
            textOk = False
            break
    print(results)
    return textOk
