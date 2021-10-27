import sqlite3
import sqlalchemy

connection = sqlite3.connect('sql1.db')
cursor = connection.cursor()

print('connected to the database')
command = """CREATE TABLE IF NOT EXISTS employee(
emp_id VARCHAR (30) PRIMARY KEY,
emp_name VARCHAR (30) NOT NULL,
department_id VARCHAR (30) NOT NULL,
FOREIGN KEY (department_id)
REFERENCES department(department_id));"""

cursor.execute(command)
print('created table employees')
command2 = """CREATE TABLE IF NOT EXISTS department(
department_id VARCHAR (30) NOT NULL PRIMARY KEY,
department_name VARCHAR (30) NOT NULL);"""

cursor.execute(command2)
print('created table department')
command3 = """CREATE TABLE IF NOT EXISTS salary(
emp_id VARCHAR (30) NOT NULL,
salary VARCHAR (30) NOT NULL,
FOREIGN KEY (emp_id)
REFERENCES employee(emp_id));"""

cursor.execute(command3)
print('created table salary')

connection.commit()

# import sqlite3
# connection = sqlite3.connect('sql1.db')
#
# cursor = connection.cursor()
#
# emp_id = [1,2,3,4,5]
# emp_name = ['mustafa', 'ibraheem', 'messi', 'yousuf', 'ahmed']
# departmet_id = ['11', '12', '13', '14', '15']
# department = ['science', 'engineering', 'teacher', 'student', 'student']
# salary = ['120000', '125000', '130000', '135000', '140000']
#
# for i in range (5):
#     cursor.execute(f'INSERT INTO IF employee VALUES ({emp_id[i]}, "{emp_name[i]}", "{departmet_id[i]}")')
#     cursor.execute(f'INSERT INTO IF department VALUES ({departmet_id[i]}, "{department[i]}")')
#     cursor.execute(f'INSERT INTO IF salary VALUES ({emp_id[i]}, "{salary[i]}")')
# connection.commit()
print()

connection.close()


# connection.close()