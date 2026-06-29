from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# Pydantic Model
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


# Dummy Database
my_posts = [
    {
        "title": "Post 1",
        "content": "Content of post 1",
        "published": True,
        "id": 1
    },
    {
        "title": "Post 2",
        "content": "Content of post 2",
        "published": True,
        "id": 2
    },
    {
        "title": "Post 3",
        "content": "Content of post 3",
        "published": True,
        "id": 3
    }
]


# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# Find Post by ID
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


# Find Post Index
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
    return None


# Get All Posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# Get Single Post
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    return {"data": post}


# Create Post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    post_dict = new_post.dict()
    post_dict["id"] = random.randint(1000, 100000)

    my_posts.append(post_dict)

    return {"data": post_dict}


# Delete Post
@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_index_post(id)

    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    my_posts.pop(index)

    return {"message": "Post deleted successfully"}


# Update Post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    post_dict = post.dict()
    post_dict["id"] = id

    my_posts[index] = post_dict

    return {"data": post_dict}