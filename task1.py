student_marks = {
    "Aren": 85,
    "David": 78,
    "Micheal": 92,
    "Franklin": 74
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
