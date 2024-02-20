from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

students = {}

Student = {
     "id": 0,
    "name": "",
    "age": 0,
    "sex": "",
    "height": 0.00
}

@app.get('/')
def home():
    return { "message": "Welcome to my Student resource API"}

@app.post('/students')
def create_student(Name: str, Age: int, Sex: str, Height: float):
     new_student = Student.copy()
     id = len(students) + 1
     new_student= {
        "Id": id,  
        "name": Name,
        "age": Age,
        "sex": Sex,
        "height": Height
    }
     students[id] = new_student
     return {"message": "Student created succesfully", "Data": new_student}

@app.get('/Students')
def get_students():
     students_arr = []
     for student in students:
         students_arr.append(students[student])
     return {"message": "Students retrieved succesfully", "Data": students_arr}

@app.get('/Students/{id}')
def get_one_student(id: int):
     student = students[id]
     return {"message": "Student retrieved succesfully", "Data": student}

@app.put('/Students/{id}')
def update_student(id: int, name:str):   
     student = students[id]
     student['name'] = name
     return {"message": "Student updated succesfully", "Data": student}

@app.delete('/Students/{id}')
def delete_student(id: int):
     student = students[id]
     del students[id]
     return {"message":" Student deleted succesfully", "Data": student}

     

     











