from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()
password = os.environ.get('MONGO_SECRET')

uri = f"mongodb+srv://adejumoridwan:{password}@cluster0.d9jr4ev.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

dictionary_collection = client["MY_DB"]["dictionary"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)





