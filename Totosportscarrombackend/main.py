from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2
from routes.user_routes import router



app = FastAPI()
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], ##used to allow request from website/frontend
    allow_credentials=True, ## allows logginsession,cookies(small data ex:typingsuggestions )
    allow_methods=["*"], #allows all fastapi methods 
    allow_headers=["*"], ##type of data to be sent,language preference(eng-us)
)