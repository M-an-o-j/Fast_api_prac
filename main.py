from fastapi import FastAPI, status
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    description : str  
    price : float
    tax: float 

app = FastAPI()

@app.get("/", status_code=200)
def Home():
    return {
        "Message":"Welcome"
    }

@app.get("/items", status_code=200)
def get_items():
    return {
        "message":"Items fetched succesfully",
    }

@app.get("/items/{id}", status_code= 200)
def get_item(id):
    return {
        "message":"Item fetched succesfully",
        "Item_Id": id
    }

@app.post("/item", status_code=201)
def create_item(item : Item):
    return {
        "message":"Created Item succesfully",
        "item": item
    }

@app.put("/todo/{id}", status_code=202)
def update_Item(id : int):
    return {
        "message":"Updated Item succesfully",
        "Item_Id": id 
    }

@app.delete("/todo/{id}", status_code=200)
def delete_Item(id: int):
    return {
        "message":"Deleted Item succesfully",
        "Item_Id": id
    }
