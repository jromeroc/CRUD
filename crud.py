#!/user/bin/python
import os.path
import time

execute = True
courses = []

def menu():
    """ View Menu """
    options = {
        0: 'Close',
        1: 'Create.',
        2: 'Edit.',
        3: 'Delete.',
        4: 'View courses.'
    }

    print("*"*30)
    print("Platzi courses catalog.")
    print("*"*30)
    print("*" * 12 + " Menu " + "*" * 12)

    for i in range(len(options)):
        print('{}. {}'.format(i, options[i]))

    option = input("Select option you will use: ")
   
    if option == '0':
        view_msn("Bye bye.")
        execute = False
    elif option == '1':
        new()
    elif option == '2':
        edit()
    elif option == '3':
       delete()
    elif option == '4':
        list_courses()
    else:
        view_msn("Option not exist.")

def new():
    """ Create course """
    name = input('Insert the course name: ')
    courses.append(name)
    view_msn("New course {} create".format(name))

def edit():
    """ Edit course """
    for i in range(len(courses)):
            print('{}. {}'.format(i, courses[i]))

    reg_edit = int(input("Select the course number do you want edit: "))
    curso_editado = input("What is the new name for this course: ")
    courses[reg_edit] = curso_editado
    view_msn("New course name {}.".format(curso_editado))

def delete():
    """ Delete course """
    for i in range(len(courses)):
        print('{}. {}'.format(i, courses[i]))
        
    reg_delete = int(input("Select the course number do you want remove: "))
    sure = input("Are you sure? Y/N: ") 

    if(sure.lower() == 'y'):
        view_msn('Course remove'.format(courses[reg_delete]))
        courses.pop(reg_delete)
    if(len(courses) == 0):
        view_msn('Not found courses:')
    else:
        view_msn('Course not removed:')
        print (" ")


def list_courses():
    """ View courses list """
    for i in range(len(courses)):
        print('{}. {}'.format(i, courses[i]))
    input('Press key for continue.')

def view_msn(msn):
    """ View message """
    os.system('cls')
    print(msn)
    time.sleep(2)
    os.system('cls')


while execute:
    os.system('cls')
    menu()

    

    
