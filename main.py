from fastapi import FastAPI
import pandas as pd

app = FastAPI()

#read data
data = pd.read_csv('data.csv')

#coba buat root home PI (get)
@app.get("/")
def root():
    return{'message':'My first API!'}

#endpoint sapaan
@app.get("/name/{name}")
def great(name):
     return{'message':f'Hai {name},how are you?'}

#http://127.0.0.1:8000/name/riki

#endpoint return data
@app.get("/data")
def get_data():
     return data.to_dict(orient='records')

#get data by id
@app.get("/data/{id}")
def search_data(id:int):
     result = data[data['id']==id]
     return{'result':result.to_dict(orient='records')}

#menambahkan data
#@app.post("/data{data}")
#def add_data(new_data:str):
 #    new_data=new_data.split('-')
     #new_row =pd.DataFrame(new_data)

     #data=pd.concat([data,new_row],ignore_index=True)

  #   return {'message':'data is updated!'}