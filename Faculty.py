''' Project on Student Evaluation System'''
import os
import math
import pickle

'''The get_menu_choice function displays the menu and gets a validated choice from the user.'''

def get_menu_choice():
    print()
    print('\n\t\t\t WELCOME TO FACULTY LOGIN!')
    print('\n\n')
    print("\t\t\t 1. ADD STUDENT PROFILE ")
    print("\t\t\t 2. EDIT STUDENT PROFILE ")
    print("\t\t\t 3. DELETE STUDENT PROFILE ")
    print("\t\t\t 4. RECORD STUDENT ACADEMICS")
    print("\t\t\t 5. ATTENDANCE ")
    print("\t\t\t 6. VIEW STUDENT PERFORMANCE")
    print("\t\t\t 7. EXIT \n\n ")

    #initialize a variable for user's choice
    choice = int(input("\t\t\t Enter choice: "))
    '''Validate the user's choice'''
    if choice < 1 or choice > 7:
        choice = int(input("\t\t\t Enter a valid choice: "))
    
    return choice

'''The AddStudentProfile function takes the data such as personal details from the user and store
    it in a Student.dat file using a list'''
def AddStudentProfile():

    if os.path.exists('Student.dat'):
        f = open("Student.dat", "r+b")
        student = pickle.load(f)

    else:
        f = open("Student.dat", 'wb')
        student = []

    print('\t\t\t STUDENT DETAILS: ')

    stu_name = input('\n\t\t\t Enter Student Name: ')
    stu_eno = (input('\n\t\t\t Enter Enrollment Number: '))
    if len(stu_eno) < 1 or len(stu_eno) > 9:
        stu_eno = input("\n\t\t\t Enter a valid Enrollment Number: ")
    stu_major = (input('\n\t\t\t Enter Student Major: '))
    city = input('\n\t\t\t Enter City: ')
    stu_phno = input("\n\t\t\t Enter Phone Number: ")
    if len(stu_phno) <1 or len(stu_phno) > 10:
        stu_phno = (input("\n\t\t\t Enter a valid Phone Number: "))

    stu_emailid = input('\n\t\t\t Enter Email Id: ')

    student.append([stu_name, stu_eno, stu_major, city, stu_phno, stu_emailid])
    f.seek(0, 0)
    pickle.dump(student, f)
    f.close()
    
    c = input("\n\t\t\t Add courses(Yes/No): ")
    while (c.lower() == 'yes' or c.lower() == 'y'):
        add_courses()
        c = input("\n\t\t\t  Continue to add courses(Yes/No): ")

'''The add_courses function takes the courses from the user and add it in courses.dat file 
    using a list'''
def add_courses():
    print("\n\n\t\t\t '''ADD COURSES'''")
    stu_eno = input("\n\n\t\t\t Enter Enrollment Number:  ")
    while (len(stu_eno) != 9):
        stu_eno = input("\n\t\t\t Enter a valid Enrollment Number: ")

    if os.path.exists('courses.dat'):
        fin = open("courses.dat", "r+b")
        courses = pickle.load(fin)

    else:
        fin = open("courses.dat", 'wb')
        courses = []
    d  =  []
    N = int(input("\n\n\t\t\t Enter Number of Entries: "))
    for i in range(1,N+1):

        print("\n\t\t\t COURSE DETAILS: ")

        course_id = input("\n\t\t\t Enter Course Id: ")
        course_name = input("\n\t\t\t Enter Course Name: ")
        course_faculty = input("\n\t\t\t Enter Course Faculty: ")
        term = input("\n\t\t\t Term: ")
        ger_cat = input("\n\t\t\t Enter GER Category: ")
        course_credits = int(input("\n\t\t\t Enter Course Credits: "))
        if course_credits > 4 or course_credits < 1:
            course_credits = int(input("\n\t\t\t Enter valid Course Credits: "))
        total_sessions = int(input("\n\t\t\t Enter Total Sessions: "))

        c = [course_id, course_name, course_faculty, term, ger_cat, course_credits, total_sessions,[]]
        d.append(c)

    courses.append([stu_eno,d])
    fin.seek(0,0)
    pickle.dump(courses, fin)
    print(courses)
    fin.close()
    print("\n\n")
    show_courses(stu_eno)

'''show_courses function  will show the course details entered by the user in the add_courses function'''   
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

'''View_Stu_Profile function would let the user see the personal details of the student'''
def View_Stu_Profile(stu_eno):

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

    print("\n")

    for i in data:
        if stu_eno == i[1]:
            print("\n\t\t\t Name: ",i[0])
            print("\t\t\t Enrollment Number: ",i[1])
            print("\t\t\t Major: ",i[2])
            print("\t\t\t Phone Number: ",i[4])
            print("\t\t\t Email_Id: ",i[5])

'''EditStudentProfile function would let the user to edit the personal information which has been previously added in 
    AddStudentProfile function'''
def EditStudentProfile():
    if os.path.exists('Student.dat'):
        f = open("Student.dat", "r+b")
        file2 = open("courses.dat", "r+b")
        student = pickle.load(f)
        data = pickle.load(file2)

    else:
        print("\n\t\t\t File Not Found!")

    
    stu_eno = (input('\n\t\t\t Enter Enrollment Number: '))
    if len(stu_eno) < 1 or len(stu_eno) > 9:
        stu_eno = input("\n\t\t\t Enter a valid Enrollment Number: ")

    View_Stu_Profile(stu_eno)

    for i in student:
        if stu_eno == i[1]:
            stu_name = input('\n\t\t\t Enter updated Student Name: ')
            i[0] = stu_name
            stu_major = (input('\n\t\t\t Enter updated Student Major: '))
            i[2] = stu_major
            city = input('\n\t\t\t Enter updated City: ')
            i[3]=city
            stu_phno = input("\n\t\t\t Enter updated Phone Number: ")
            i[4]=stu_phno
            stu_emailid = input('\n\t\t\t Enter updated Email Id: ')
            i[5]=stu_emailid

    ch = input("\n\t\t\t Update Marks ( Yes/ No): ")

    while ch.lower() == 'y' or ch.lower() == 'yes':

        for j in data:
            if stu_eno == j[0]:
                
                show_courses(stu_eno)
                course_id = input("\n\t\t\t Enter Course Id: ")

                for c in j[1]:
                    if course_id == c[0]:
                        stu_assi =int(input('\n\t\t\t Enter Updated Assignment Marks out of 20: '))
                        while stu_assi >20 or stu_assi < 0:
                            stu_assi =int(input('\n\t\t\t Enter Valid Assignment Marks out of 20: '))

                        stu_act = int(input('\n\t\t\t Enter Updated Class Activity Marks out of 10: '))
                        while stu_act >10 or stu_act < 0:
                            stu_assi =int(input('\n\t\t\t Enter Valid Class Activity Marks out of 10: '))
                        
                        stu_mid = int(input('\n\t\t\t Enter Updated Midterm Marks out of 30: '))
                        while stu_mid >30 or stu_mid < 0:
                            stu_mid = int(input('\n\t\t\t Enter Valid Midterm Marks out of 30: '))

                        stu_end = int(input("\n\t\t\t Enter Updated Endterm Marks out of 40: "))
                        while stu_end >40 or stu_end < 0:
                            stu_end = int(input("\n\t\t\t Enter Valid Endterm Marks out of 40: "))

                        tot_marks=stu_assi+stu_mid+stu_end+stu_act
                        Percent=(tot_marks)


                        if tot_marks >= 92:
                            print("\n\t\t\t Grade: A+")
                            grade = 'A+'
                        elif tot_marks>= 84 and tot_marks <= 91:
                            print("\n\t\t\t Grade: A-")
                            grade = 'A-'
                        elif tot_marks >=76 and tot_marks <= 83:
                            print("\n\t\t\t Grade: B+")
                            grade = 'B+'
                        elif tot_marks >= 68 and tot_marks <= 75:
                            print("\n\t\t\t Grade: B-")
                            grade = 'B-'
                        elif tot_marks >= 60 and tot_marks <= 67:
                            print("\n\t\t\t Grade: C+")
                            grade = 'C+'
                        elif tot_marks >= 52 and tot_marks <= 59:
                            print("\n\t\t\t Grade: C-")
                            grade = 'C-'
                        elif tot_marks < 52:
                            grade = 'F'


                        academic = [stu_assi,stu_act,stu_mid,stu_end,tot_marks,Percent, grade]
                        c[7] = academic
                ch = input("\n\t\t\t Update Marks ( Yes/ No): ")

    pickle.dump(student, f)
    f.close() 

'''Delete_Entry function would let the user to delete the information which was added in AddStudentProfile function'''
def Delete_Entry():
    if os.path.exists("Student.dat"):
        f = open("Student.dat", "r+b")
        data = pickle.load(f)

        stu_eno = input("\n\t\t\t Enter Enrollment Number to be Deleted: ")
        if len(stu_eno) < 1 or len(stu_eno) > 9:
            stu_eno = input("\n\t\t\t Enter a valid Enrollment Number: ")

        View_Stu_Profile(stu_eno)

        found = False
        pos1 = None

        for i in data:
            if stu_eno == i[0]:
                pos1 = i
                found = True
                break

        
        if not True:
            print("\n\t\t\t '''Enrollment Number Not found!'''")

        else:
            data.remove(1)

            print("\n\t\t\t '''Data Deleted Successfully!")

        f.seek(0,0)
        pickle.dump(data, f)
        f.close()

    else:
        print("\n\t\t\t File Not Found!")

'''AddStudentEntry function will let the user to enter marks of the student and to calculate the grades'''
def AddStudentEntry():
    stu_eno = (input('\n\t\t\t Enter Enrollment Number to be searched: '))

    View_Stu_Profile(stu_eno)

    f1=open("courses.dat","r+b")
    data = pickle.load(f1)

    for i in data:
        if stu_eno == i[0]:

            show_courses(stu_eno)
            course_id = input("\n\t\t\t Enter Course Id whose Marks are to be entered: ")

            for c in i[1]:
                if course_id  == c[0]:

                    stu_assi =int(input('\n\t\t\t Enter Assignment Marks out of 20: '))
                    if stu_assi >20 or stu_assi < 0:
                            stu_assi =int(input('\n\t\t\t Enter Valid Assignment Marks out of 20: '))

                    stu_act = int(input('\n\t\t\t Enter Class Activity Marks out of 10: '))
                    if stu_act >10 or stu_act < 0:
                            stu_assi =int(input('\n\t\t\t Enter Valid Class Activity Marks out of 10: '))
                        
                    stu_mid = int(input('\n\t\t\t Enter Midterm Marks out of 30: '))
                    if stu_mid >30 or stu_mid < 0:
                            stu_mid = int(input('\n\t\t\t Enter Valid Midterm Marks out of 30: '))

                    stu_end = int(input("\n\t\t\t Enter Endterm Marks out of 40: "))
                    if stu_end >40 or stu_end < 0:
                            stu_end = int(input("\n\t\t\t Enter Valid Endterm Marks out of 40: "))

                    tot_marks=stu_assi+stu_mid+stu_end+stu_act
                    Percent=(tot_marks)

                    if tot_marks >= 92:
                        print("\n\t\t\t Grade: A+")
                        grade = 'A+'
                    elif tot_marks>= 84 and tot_marks <= 91:
                        print("\n\t\t\t Grade: A-")
                        grade = 'A-'
                    elif tot_marks >=76 and tot_marks <= 83:
                        print("\n\t\t\t Grade: B+")
                        grade = 'B+'
                    elif tot_marks >= 68 and tot_marks <= 75:
                        print("\n\t\t\t Grade: B-")
                        grade = 'B-'
                    elif tot_marks >= 60 and tot_marks <= 67:
                        print("\n\t\t\t Grade: C+")
                        grade = 'C+'
                    elif tot_marks >= 52 and tot_marks <= 59:
                        print("\n\t\t\t Grade: C-")
                        grade = 'C-'
                    elif tot_marks < 52:
                        grade = 'F'

                    academic = [stu_assi,stu_act,stu_mid,stu_end,tot_marks,Percent, grade]
                    c[7] = academic            
        print("\n")

    f1.seek(0,0)
    pickle.dump(data,f1)            
                
    f1.close()

'''StudentAttend function would let the user to enter the attendance as per the course of the student'''
def StudentAttend():

    if os.path.exists('StudentAttend.dat'):
        f = open("StudentAttend.dat", "r+b")
        attendance = pickle.load(f)

    else:
        f = open("StudentAttend.dat", 'ab')
        attendance = []

    stu_eno = (input('\n\t\t\t Enter Enrollment Number to be searched: '))
    View_Stu_Profile(stu_eno)
    
    f2 = open("courses.dat", "rb")
    data1 = pickle.load(f2)
    show_courses(stu_eno)

    for i in data1:
        if stu_eno==i[0]:

            show_courses(stu_eno)
            course_id = (input('\n\t\t\t Enter Course id to be searched: '))
            for c in i[1]:
                
                if course_id==c[0]:

                    stu_attend = int(input('\n\t\t\t Enter the sessions attended: '))
                    tot_sessions=c[6]
                    per_attend=(stu_attend/tot_sessions)*100

                    #c[1] : Course Name, c[7] = Academic Marks and Grade
                    d = [stu_eno,course_id,c[1],c[7],per_attend]
                    attendance.append(d)
    f.seek(0,0)
    pickle.dump(attendance,f)
    f.close()

'''student_performance function would let the user see the academic performance of the student'''
def student_performance():

    if os.path.exists("StudentAttend.dat"):
        f = open("StudentAttend.dat", "r+b")
        academic = pickle.load(f)

    else:
        print("\n\t\t\t File Not Found!")

    stu_eno = input("\n\t\t\t Enter Enrollment Number of the Student: ")
    if len(stu_eno) < 1 or len(stu_eno) > 9:
        stu_eno = input("\n\t\t\t Enter a valid Enrollment Number: ")
    View_Stu_Profile(stu_eno)
    print("\n\n")

    file2 = open("Student.dat", "rb")
    data = pickle.load(file2)

    for i in data:
        if stu_eno == i[1]:
            print('-'*75)
            print('%16s'%'NAME |','%15s'%'ENROLLMENT NUMBER |','%9s'%'MAJOR |','%16s'%'PHONE NUMBER |','%12s'%'EMAIL ID')
            print('-'*75)
            print('%16s'%i[0],'%15s'%i[1],'%9s'%i[3],'%16s'%i[2],'%12s'%i[5])

    for j in academic:
        if stu_eno == j[0]:

            show_courses(stu_eno)
            courseid = input("\n\t\t\t Enter Course Id: ")
            if courseid == j[1]:
                print('-'*70) 
                print('%16s'%'COURSE NAME |','%15s'%'TOTAL MARKS |','%9s'%'GRADE |','%25s'%'PERCENTAGE ATTENDANCE |')
                print('-'*70) 
                print('%16s'%j[2],'%15s'%j[3][4],'%9s'%j[3][6],'%25s'%j[4])
choice = 0

while choice != 7:
    #Get the user's menu choice
    choice = get_menu_choice()

    #Process the choice

    if (choice == 1):
        AddStudentProfile()

    elif (choice == 2):
        EditStudentProfile()

    elif (choice == 3):
        
        Delete_Entry()

    elif (choice == 4):
        AddStudentEntry()

    elif (choice == 5):
        StudentAttend()

    elif (choice == 6):
        student_performance()

