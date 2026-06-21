# This task is used to demonstrate object-oriented programming by creating a student report system
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}  # Empty dict to store subject: grade pairs

    def add_grade(self, subject, grade):
        """Add or update a grade for a subject"""
        self.grades[subject] = grade
        print(f" Added {subject}: {grade} for {self.name}")

    def display_report_card(self):
        """Show the full report card"""
        print(f"\n{'='*40}")
        print(f"REPORT CARD - {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"{'='*40}")

        if not self.grades:
            print("No grades added yet")
        else:
            for subject, grade in self.grades.items():
                print(f"{subject}: {grade}")
        print(f"{'='*40}\n")


# How to USE it:
student1 = Student("Gayu", "137")
student1.add_grade("Math", 95)
student1.add_grade("Python", 98)
student1.add_grade("Physics", 88)
student1.display_report_card()

# Update a grade
student1.add_grade("Physics", 92)
student1.display_report_card()
