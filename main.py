from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title:str
    description:str
    published:bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


@app.get("/posts")
async def posts():
    return {"data" : "These are your posts..."}


@app.post("/posts")
async def create_post(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"data" : new_post}