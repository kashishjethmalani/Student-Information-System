import imp
import pickle
from getpass import getpass
import subprocess
import os

def login():
    print("\n\t\t\t\t '''MAIN MENU'''")
    print("\n\t\t\t 1. FACULTY | 2. STUDENT | 3.EXIT")

    ch = int(input("\n\t\t\t Enter choice: "))
    return ch

ch = 0
while ch != 3:
    ch =  login()
    if (ch == 1):
        faculty_pass = getpass("\t\t\t Enter Password: ")
        if (faculty_pass == 'GUEST'):
            import Faculty

        else:
            print("\n\t\t\t WRONG PASSWORD!")
        
    elif (ch == 2):
        stu_pass = getpass("\t\t\t Enter Password: ")
        if (stu_pass == 'GUEST'):
            import Student

        else:
            print("\n\t\t\t WRONG PASSWORD!")