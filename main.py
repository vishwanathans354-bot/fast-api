from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


# Pydantic Model
class Post(BaseModel):
    title: str
    content: str
    published: bool =True
    
    
my_posts = [{"title": "Post 1", "content": "Content of post 1", "published": True, "id": 1},
            {"title": "Post 2", "content": "Content of post 2", "published": True, "id": 2},
            {"title": "Post 3", "content": "Content of post 3", "published": True, "id": 3}
        
            ]


@app.get("/posts/{id}")
def get_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return {"post_detail": post}
        
  

    

# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}




# Get All Posts
@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


# Create Post 
@app.post("/posts")
def create_posts(new_post: Post):
    return {
        "data": f"Post is created with title '{new_post.title}', "
                f"content '{new_post.content}', "
                f"published status '{new_post.published}'"
    }


#