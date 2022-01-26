from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 20,
        "year": "year 12"
    },
}

class Students(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudents(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/students/{student_id}")
def get_student(student_id: int = Path(None, description="The id of the student you want to view", gt=0)):
    return students[student_id]

# @app.get("/get-by-name")
# def get_student(student_name: str):
#     for student in students.values():
#         if student["name"] == student_name:
#             return student
#     return {"message": "Student not found"}

@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"message": "Student not found"}


# create student
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Students):
    if student_id not in students:
        students[student_id] = student
        return students[student_id]
    return {"Error": "Student already exists"}

#edit student
@app.put("/edit-student/{student_id}")
def edit_student(student_id: int, student: UpdateStudents):
    if student_id in students:
        if student.name != None:
            students[student_id]["name"] = student.name

        if student.age != None:
            students[student_id]["age"] = student.age

        if student.year != None:
            students[student_id]["year"] = student.year
    return {"Error": "Student does not exist"}


# delete student
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id in students:
        del students[student_id]
        return {"message": "Student deleted"}
    return {"Error": "Student does not exist"}

 