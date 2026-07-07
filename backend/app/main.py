from fastapi import FastAPI
from sqlalchemy import text

from .database import engine

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Production DevOps Project"}

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.get("/users")
def users():
    with engine.connect() as conn:
        result = conn.execute(text("select * from users"))
        return [dict(row._mapping) for row in result]
