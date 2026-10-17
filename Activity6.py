class Student:
    def __init__(self, grade):
        self.__grade = grade

    def study(self):
        print("Student is studying.")

    def get_grade(self):
        return self.__grade


class CollegeStudent(Student):
    def study(self):
        print("College student is studying programming.")


student = Student(90)
college_student = CollegeStudent(95)

student.study()
college_student.study()