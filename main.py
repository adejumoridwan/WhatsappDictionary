from fastapi import FastAPI, Form
import requests
from utils import send_message, logger
from dotenv import load_dotenv
import os
import json
from typing import List
import re
from models import dictionary_collection

load_dotenv()

app = FastAPI()
whatsapp_number = os.getenv("TO_NUMBER")
api_key = os.getenv("DICTIONARY_API_KEY")

@app.post("/message")
async def reply(Body: str = Form()):
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{Body}?key={api_key}"
    flag="Please give a valid word"
    
    if Body.isalpha():
        response = requests.get(url)
        # Extract the JSON data from the response
        data = response.json()
        
        definition = data[0]["shortdef"][0]

        send_message(whatsapp_number, definition)

        dictionary_db = {"word":Body, "definition":definition}
        dictionary_collection.insert_one(dictionary_db)

        logger.info(f"Definition:{definition}")

    else:
        return send_message(whatsapp_number, flag)
    
    
    return ""

    
    

