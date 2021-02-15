from utils import database_back
from login_error import ReCheckPassword,ReCheckUserName
from datetime import date,time,datetime,timezone,timedelta
from tkinter import *

login=datetime.now()
print(login.strftime('%Y-%m-%d %H:%M'))


print("This Page used only for Registering the Employees details and Retrieving in runtime and logging into the Company Details....")
print("You can able to Add Company Material Or to view.Only if you login successfully....")


USER_CHOICE='''
    -'r' to Registering Employee Details
    -'l' to Add  Login Details
    -'e' to Add Employee Details
    -'t' to Update Timesheet
    -'vr' For Reading Registered Details
    -'vl' For Reading Login Details
    -'ve' For Viewing Employee Table
    -'vt' For Viewing Timesheet Table
    -'log' for login
    -'m' to Add Material Details
    -'vm' For Viewing Material Details
Your_Choice = '''

emp_lis={}

def menu():
    database_back.create_reg_table()
    database_back.create_login_table()
    database_back.create_employees_table()
    database_back.create_timesheet_table()
    database_back.create_material()
    database_back.get_info_reg()
    database_back.get_info_employee_table()
    database_back.get_timesheet_table()
    database_back.get_info_login()
    database_back.get_material_detail()

    user_input=input(USER_CHOICE)
    while user_input !='q':
        if user_input=='r':
            add_register()
        if user_input=='l':
            add_login()
        if user_input=='e':
            add_employee()
        if user_input=='t':
            add_timesheet()
        if user_input=='vr':
            view_info()
        if user_input=='vl':
            view_login()
        if user_input=='ve':
            view_employee()
        if user_input=='vt':
            view_timesheet()
        if user_input=='log':
            name = input("user_name : ")
            passc=input("password:")
            login(name,passc)
        if user_input=='m':
            add_materials()
        if user_input=='vm':
            view_materials()

        user_input=input(USER_CHOICE)
def click(employee_id, name, dob, email):
    database_back.insert_reg(employee_id, name, dob, email)

def add_register():
    root = Tk()
    a = Label(root, text="Registeration").grid(column=0, row=0)
    employee_id = StringVar()
    emp_id = Entry(root, width=12, textvariable=employee_id).grid(column=0, row=1)
    name = StringVar()
    name_e = Entry(root, width=12, textvariable=name).grid(column=0, row=2)
    dob = StringVar()
    dob_e = Entry(root, width=12, textvariable=dob).grid(column=0, row=3)
    email= StringVar()
    email_e= Entry(root, width=12, textvariable=email).grid(column=0, row=4)
    button = Button(root, text="submit", command=lambda:click(employee_id.get(), name.get(), dob.get(), email.get())).grid(column=0, row=5)
    root.mainloop()


def click1(employee_name,password):
    database_back.insert_login(employee_name,password)


def add_login():
    root=Tk()
    a=Label(root,text="login").grid(column=0,row=0)
    name=StringVar()
    name_e=Entry(root,width=12,textvariable=name).grid(column=0,row=1)
    password=StringVar()
    password_e=Entry(root,width=12,textvariable=password).grid(column=0,row=2)
    button=Button(root,text="add",command=lambda:click1(name.get(),password.get()) ).grid(column=0,row=3)
    root.mainloop()


def click2(dept_name,dept_code):
    database_back.insert_employees_table(dept_name,dept_code)


def add_employee():
    root=Tk()
    a=Label(root,text="employee").grid(column=0,row=0)
    dept_name=StringVar()
    dep_name=Entry(root,width=12,textvariable=dept_name).grid(column=0,row=1)
    dept_code=StringVar()
    dep_code=Entry(root,width=12,textvariable=dept_code).grid(column=0,row=2)
    button=Button(root,text="add",command=lambda:click2(dept_name.get(),dept_code.get())).grid(column=0,row=3)
    root.mainloop()


def add_timesheet():
    log_in_time=input("Time You Made Entry : ")
    log_out_time=input("Time you Left : ")
    database_back.insert_timsheet_table(log_in_time,log_out_time)


def add_materials():
    name_of_material=input("Enter the Material Name : ")
    type=input("Enter the Type of Material : ")
    grid=input("Enter the Availability of Stock : ")
    prize=input("Enter the Prize of Material : ")
    database_back.insert_details(name_of_material,type,grid,prize)


def view_info():
    for ry in database_back.get_info_reg():
        print(f"  employee_id: {ry['employee_id']} ,  name: {ry['name']}  , d.o.b : {ry['dob']}  ,  email id : {ry['email']}")


def view_login():
    for lg in database_back.get_info_login():
        print(f"employee_name : {lg['name']} , password: {lg['password']}")


def view_employee():
    for el in database_back.get_info_employee_table():
        print(f"dept name : {el['dept_name']},  dept code : {el['dept_code']}")


def view_timesheet():
    for ts in database_back.get_timesheet_table():
        print(f"login time : {ts['log_in_time']} ,  logout time : {ts['log_out_time']}")


def view_materials():
    for gm in database_back.get_material_detail():
        print(f" name : {gm['name_of_material']} ,  type:{gm['type']}  , stock : {gm['grid']}  , prize: {gm['prize']}")


def login(name,passcode):
    for lg in database_back.get_info_login():
        emp_lis[lg['name']]=lg['password']
    if name in emp_lis:
        if passcode==emp_lis[name]:
            print("logged in successfully...")
            print("Now You Have a Access to enter the Comapny Material details...")
        else:
            raise ReCheckPassword
    else:
            raise ReCheckUserName




menu()


