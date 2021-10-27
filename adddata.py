import sqlite3
connection = sqlite3.connect('sql1.db')

cursor = connection.cursor()

emp_id = [1,2,3,4,5]
emp_name = ['mustafa', 'ibraheem', 'messi', 'yousuf', 'ahmed']
departmet_id = ['11', '12', '13', '14', '15']
department = ['science', 'engineering', 'teacher', 'student', 'student']
salary = ['120000', '125000', '130000', '135000', '140000']

for i in range (5):
    cursor.execute(f'INSERT INTO employee VALUES ({emp_id[i]}, "{emp_name[i]}", "{departmet_id[i]}")')
    cursor.execute(f'INSERT INTO department VALUES ({departmet_id[i]}, "{department[i]}")')
    cursor.execute(f'INSERT INTO salary VALUES ({emp_id[i]}, "{salary[i]}")')
connection.commit()
connection.close()
