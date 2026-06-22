# 🎓 Student Report Card System

A simple Python project demonstrating **Object-Oriented Programming (OOP)** concepts by creating a student report card management system.

## 📌 Features

* 👨‍🎓 Create student records
* 🆔 Store student name and ID
* ➕ Add grades for multiple subjects
* 🔄 Update existing grades
* 📋 Display a formatted report card
* 🗂 Store grades using Python dictionaries

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/student-report-system.git
cd student-report-system
```

### Run the Program

```bash
python3 student_report.py
```

---

## 🧠 Concepts Used

| Concept                  | Purpose                              |
| ------------------------ | ------------------------------------ |
| Classes & Objects        | Creating Student objects             |
| `__init__()` Constructor | Initializing student data            |
| Instance Variables       | Storing name, ID, and grades         |
| Dictionaries             | Managing subject-grade pairs         |
| Methods                  | Adding grades and displaying reports |
| String Formatting        | Creating clean report card output    |
| Loops                    | Displaying all subjects and grades   |

---

## 📂 Project Structure

```text
student_report.py
README.md
```

---

## 💻 Example Output

```text
 Added Math: 95 for Gayu
 Added Python: 98 for Gayu
 Added Physics: 88 for Gayu

========================================
REPORT CARD - Gayu
Student ID: 137
========================================
Math: 95
Python: 98
Physics: 88
========================================

 Added Physics: 92 for Gayu

========================================
REPORT CARD - Gayu
Student ID: 137
========================================
Math: 95
Python: 98
Physics: 92
========================================
```

---

## 🔍 How It Works

1. Create a student object.
2. Add subject grades using the `add_grade()` method.
3. Grades are stored in a dictionary as:

```python
{
    "Math": 95,
    "Python": 98,
    "Physics": 92
}
```

4. Display the report card using the `display_report_card()` method.
5. If a subject already exists, its grade is automatically updated.

---

## 📖 Sample Usage

```python
student1 = Student("Gayu", "137")

student1.add_grade("Math", 95)
student1.add_grade("Python", 98)
student1.add_grade("Physics", 88)

student1.display_report_card()
```

---

## 🎯 Learning Objectives

This project helps understand:

* Object-Oriented Programming (OOP)
* Classes and Objects
* Constructors
* Methods
* Dictionaries
* Data Encapsulation
* Python String Formatting

---

### 👩‍💻 Author

Built as part of Python Intermediate Learning – OOP Practice Project.
