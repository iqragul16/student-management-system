import os
import json

students = []

def load_students():
    global students
    try:
        f = open("students.json", "r")
        students = json.load(f)
        f.close()
    except:
        print("File not found, creating new list")
        students = []

def save_students():
    f = open("students.json", "w")
    json.dump(students, f)
    f.close()

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added")

def show_students():
    if len(students) == 0:
        print("No students found")

    for s in students:
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Marks:", s["marks"])
        print("-------------------")

def find_student():
    name = input("Enter name to search: ")

    found = False
    for s in students:
        if s["name"] == name:
            print("Student found")
            print(s)
            found = True

    if found == False:
        print("Student not found")

def delete_student():
    name = input("Enter student name to delete: ")

    for s in students:
        if s["name"] == name:
            students.remove(s)
            print("Student deleted")

def update_student():
    name = input("Enter student name to update: ")

    for s in students:
        if s["name"] == name:
            new_marks = input("Enter new marks: ")
            s["marks"] = new_marks
            print("Marks updated")

def average_marks():
    total = 0
    for s in students:
        total = total + int(s["marks"])

    avg = total / len(students)
    print("Average marks:", avg)

def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Find Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Average Marks")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            find_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            update_student()

        elif choice == "6":
            average_marks()

        elif choice == "7":
            save_students()

        elif choice == "8":
            break

        else:
            print("Invalid choice")

load_students()
menu()