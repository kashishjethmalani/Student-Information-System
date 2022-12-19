''' Project on Student Evaluation System '''
import os
import math
import pickle
import matplotlib.pyplot as py

def show_courses(stu_eno):
    f = open("courses.dat","rb")
    courses = pickle.load(f)
    for i in courses:
        if stu_eno == i[0]:
            print('-'*75)
            print('%16s'%'COURSE ID |','%15s'%'COURSE NAME |','%9s'%'TERM |','%16s'%'FACULTY |','%12s'%'CREDITS')
            print('-'*75)
            for j in i[1]:
                print('%16s'%j[0],'%15s'%j[1],'%9s'%j[3],'%16s'%j[2],'%12s'%j[5])
    f.close()
    print('\n')

''' The View_Stu_Profile function asks for the Enrollment Number as the input and displays the personal details of that particular student from the file Student.dat'''        
def View_Stu_Profile():

    if os.path.exists("Student.dat"):
        file_in = open("Student.dat", "rb")
        data = pickle.load(file_in)

    else:
        print("\n\t\t\t File Not Found!")

    if os.path.exists("courses.dat"):
        file2 = open("courses.dat", "rb")
        course = pickle.load(file2)

    else:
        print("\n\t\t\t File Not Found!")

    stu_eno = input("\n\t\t\t Enter Enrollment Number: ")
    if len(stu_eno) < 1 or len(stu_eno) > 9:
        stu_eno = input("\n\t\t\t Enter a valid Enrollment Number: ")

    for i in data:
        if stu_eno == i[1]:
            print("\n\t\t\t Name: ",i[0])
            print("\t\t\t Enrollment Number: ",i[1])
            print("\t\t\t Major: ",i[2])
            print("\t\t\t Phone Number: ",i[4])
            print("\t\t\t Email_Id: ",i[5])


''' The View_Acad_Perform function asks for the Enrollment Number as the input and displays the course details and represents the marks using a bar plot. '''
def View_Acad_Perform():

    if os.path.exists("StudentAttend.dat"):
        file_in = open("StudentAttend.dat", "r+b")
        academic = pickle.load(file_in)
        fc = open("courses.dat",'rb')
        course = pickle.load(fc)

    else:
        print("\n\t\t\t ERROR!")

    stu_eno = input("\n\t\t\t Enter Enrollment Number: ")
    for i in academic:
        if stu_eno == i[0]:

            show_courses(stu_eno)
            course_id = (input("\n\t\t\t Enter Course Id: "))

            if course_id == i[1]:
                # marks = [assignment, activity, midsem, endsem, total marks, percentage]
                marks = i[3]
                course_name = i[2]
                attendance = i[4]

                x=[1, 2, 3, 4]
                y=[i[3][0], i[3][1], i[3][2], i[3][3]]
                tick_label= ['Assignment','Activity','Midsem','Endsem']
                py.bar(x,y,tick_label=tick_label,width=0.8)
                py.xlabel('x')
                py.ylabel('marks')
                py.show()

            else:
                print("\n\t\t\t No record found!")

ch = 'y'   
while ch.lower() == 'y' or ch.lower() == 'yes':
    print()
    print("\n\t\t\t WELCOME TO STUDENT LOGIN!")
    print("\n\n")
    print("\t\t\t  1. VIEW STUDENT PROFILE")
    print("\t\t\t  2. VIEW ACADEMIC PERFORMANCE")
    print("\t\t\t  3. EXIT\n")

    choice = int(input("\t\t\t Enter choice: "))

    if choice == 1:
        View_Stu_Profile()

    elif choice == 2:
        View_Acad_Perform()

    ch = (input("\t\t\t Run again(Yes/ No): "))

    


