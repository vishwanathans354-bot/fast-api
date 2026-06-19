from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()
class item(BaseModel):
    name:str
    price:float
    product: str
    


@app.get("/")
def viswa():
    return {'message': 'Hello, World!'} 


@app.get("/next")
def next():
    return {"message": "second route create successfully"}



@app.get("/item/{item_id}" )
def id(item_id: int, query: str = None , name: str = None):
     return {"item_id": item_id, "query": query, "name": name}
 
 
@app.get("/products")
def list_products(skip: int = 0, limit: int = 10):
     return {"skip": skip, "limit": limit}
  
   
@app.post("/update")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}


@app.post("/create")
def create_item(item: item):
    return item



