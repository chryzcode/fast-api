from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 20,
        "classs": "year 12"
    },
}

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
