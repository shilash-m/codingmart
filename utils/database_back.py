from utils.database import DataBaseConnection

def create_reg_table():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' CREATE TABLE reg 
        (
        employee_id VARCHAR(255) PRIMARY KEY,
        name TEXT NOT NULL,
        d_o_b DATE NOT NULL,
        email_id VARCHAR(255) NOT NULL
        )
        ''')


def create_login_table():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' CREATE TABLE login 
        (
        name TEXT NOT NULL,
        password VARCHAR(255) NOT NULL
        )
        ''')


def create_employees_table():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' CREATE TABLE employee_tab
        (
        dept_name VARCHAR(255) NOT NULL,
        dept_code VARCHAR(255) NOT NULL       
        )
        ''')


def create_timesheet_table():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' CREATE TABLE timesheet_tabl
        (
        log_in_time TIME(0) NOT NULL,
        log_out_time TIME(0) NOT NULL
        )
        ''')


def create_material():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' CREATE TABLE material_details
        (
        name_of_material varchar(255),
        type VARCHAR(255), 
        grid varchar(255),
        prize VARCHAR(255)
        )
        ''')


def insert_reg(employee_id,name,d_o_b,email_id):
    with DataBaseConnection('test1.db') as connection:
        cursor = connection.cursor()
        cursor.execute(''' INSERT INTO reg 
        (
         employee_id ,
         name,
         d_o_b,
         email_id
        ) 
        VALUES
        (?,?,?,?)''',(employee_id,name,d_o_b,email_id)

        )


def insert_login(employee_name,password):
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' INSERT INTO login(
        name ,
        password 
        ) 
        VALUES
        (?,?)  ''',(employee_name,password)

        )


def insert_employees_table(dept_name,dept_no):
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' INSERT INTO employee_tab(
        dept_name,
        dept_code
        ) VALUES 
        (?,?)''',(dept_name,dept_no)

        )


def insert_timsheet_table(log_in_time,log_out_time):
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' INSERT INTO timesheet_tabl
        (
        log_in_time ,
        log_out_time 
        
        ) VALUES 
        (?,?)''',(log_in_time,log_out_time)
        
        )


def insert_details(name_of_material,type,grid,prize):
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(''' INSERT INTO material_details 
        (
        name_of_material,
        type ,
        grid,
        prize
        ) VALUES 
        (?,?,?,?)''',(name_of_material,type,grid,prize)

        )


def insert_filters(prize,stock):
    with DataBaseConnection('test1.db') as connection:
        cursor = connection.cursor()
        cursor.execute(''' INSERT INTO grid
        (
        prize,
        stock
        ) VALUES 
        (?,?)''',(prize,stock)

          )


def get_info_reg():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(' SELECT employee_id,name,d_o_b ,email_id FROM reg')
        details=[{'employee_id':row[0],'name':row[1] ,'d_o_b':row[2],'email_id':row[3]} for row in cursor.fetchall()]
    return details


def get_info_login():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(' SELECT name,password FROM login')
        detail=[{'name':row[0],'password':row[1]} for row in cursor.fetchall()]
    return detail


def get_info_employee_table():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(' SELECT dept_name,dept_code FROM employee_tab')
        details=[{'dept_name':row[0],'dept_code':row[1] }for row in cursor.fetchall()]
    return details


def get_timesheet_table():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(' SELECT log_in_time,log_out_time FROM timesheet_tabl')
        details=[{'log_in_time':row[0],'log_out_time':row[1]} for row in cursor.fetchall()]
    return details


def get_material_detail():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(' SELECT name_of_material,type,grid,prize FROM material_details')
        details=[{'name_of_material':row[0],'type':row[1],'grid':row[2],'prize':row[3]} for row in cursor.fetchall()]
    return details


def get_filter():
    with DataBaseConnection('test1.db') as connection:
        cursor=connection.cursor()
        cursor.execute(' SELECT prize,stock FROM grid')
        details=[{'prize':row[0],'stock':row[1]} for row in cursor.fetchall()]
    return details


print("Entered webpage at : ")