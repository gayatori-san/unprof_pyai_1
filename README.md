📚 Student Report System
A minimal, object-oriented student grade management system built in Python.
✨ What It Does
👤 Create student profiles with name and student ID
➕ Add or update grades for any subject
📊 Display a formatted report card with all grades
🔄 Update existing grades seamlessly
🚀 Installation & Usage
Clone the repository:
bash
git clone https://github.com/your-username/student-report-system.git
cd student-report-system
Run the program:
bash
python3 student_report.py
🧠 OOP Concepts Used
Table
Concept	Where It's Used
Class	Student class encapsulates all student data and behavior
__init__	Constructor initializes name, student_id, and grades dictionary
self	Instance variables shared across all methods
Dictionary	grades dict stores subject-grade pairs
Methods	add_grade() and display_report_card() are instance methods
String formatting	f-strings and string multiplication for clean report card UI
📁 File Structure
plain
student_report.py
Single-file implementation — no external dependencies needed!
📝 Example Output
plain
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
🔧 Code Walkthrough
Python
class Student:
    def __init__(self, name, student_id):
        # Initialize student with name, ID, and empty grades dict
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        # Add or overwrite a grade for a subject
        self.grades[subject] = grade

    def display_report_card(self):
        # Print formatted report card with all grades
        ...
💡 Future Enhancements
[ ] Calculate GPA / average grade
[ ] Save/load grades to JSON file
[ ] Add multiple students support
[ ] Grade validation (0-100 range)
[ ] Subject category grouping
Made with ☕ and Python classes.
