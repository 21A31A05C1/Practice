
class Person:
    def __init__(self,name,department):
        self.name = name 
        self.department = department
class Teacher(Person):
    def __init__(self,name,ID,department):
        super().__init__(name,department)
        self.ID = ID
        
class Student(Person):
    def __init__(self,name,rollNo,department):
        super().__init__(name,department)
        self.rollNo = rollNo
        
class College:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
    
    def enrollStudent(self,name,rollNo,department): 
        st = Student(name,rollNo,department)
        self.students.append(st)
        
    def enrollTeacher(self,name,ID,department): 
        te = Teacher(name,ID,department)
        self.teachers.append(te)
        
    def deleteStudent(self,rollNo):
        searchResult = self.searchStudent(rollNo)
        if(searchResult):
            print(searchResult.name," student of rollNo ",searchResult.rollNo, "  REMOVED...")
            self.students.remove(searchResult)
        else:
            print("Student doesnot exist...")
            
    def deleteTeacher(self,ID):
        searchResult = self.searchTeacher(rollNo)
        if(searchResult):
            print(searchResult.name," student of rollNo ",searchResult.ID, "  REMOVED...")
            self.teacher.remove(searchResult)
        else:
            print("Teacher doesnot exist...")
            
    def searchStudent(self,rollNo):
        for stud in self.students:
            if stud.rollNo == rollNo:
                return stud 
        return None
        
    def searchTeacher(self,ID):
        for stud in self.teachers:
            if stud.ID == ID:
                return stud 
        return None
        
    def studentsList(self):
        for stud in self.students:
            print("Name: " ,stud.name, " | ", "RollNo : ", stud.rollNo," | ","Department :", stud.department )
    
    def teachersList(self):
        for stud in self.teachers:
            print("Name: " ,stud.name, " | ", "RollNo : ", stud.ID," | ","Department :", stud.department )

pr = College("Pragati")

while True:
    print("Select one option:")
    print('''1:Exit() \n 2:Enroll a student \t 3:Remove a student \t 
            4:View Student List \t 5:Enroll a Teacher \t 6:Remove a teacher \t 7:View Teacher List''')
    opt = int(input())
    if opt==1:
        exit()
    elif opt==2:
        name = input("Enter Name :")
        rollNo = input("Enter RollNo :")
        department = input("Enter Department :")
        pr.enrollStudent(name,rollNo,department)
        print("Student : ",name," | RollNo : ",rollNo," | Department : ",department," ADDED++")
    elif opt==3:
        rollNO = input("Enter the rollNO of to Delete : ")
        pr.deleteStudent(rollNO)
    elif opt==4:
        print("<--------LIST OF STUDENTS OF ",pr.name," COLLEGE-------->")
        pr.studentsList()
    elif opt==5:
        name = input("Enter Name :")
        ID = input("Enter ID :")
        department = input("Enter Department :")
        pr.enrollTeacher(name,ID,department)
        print("Teacher : ",name," | ID : ",ID," | Department : ",department," ADDED++")
    elif opt==6:
        ID = input("Enter the ID of to Delete : ")
        pr.deleteStudent(ID)
    elif opt==7:
        print("<--------LIST OF TEACHERS OF ",pr.name," COLLEGE-------->")
        pr.teachersList()
        
        