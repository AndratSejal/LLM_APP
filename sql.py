#sqlite3 by deafult comes along with python setup
import sqlite3

#connect to sqlite
connection=sqlite3.connect("student.db")

#Create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

#Creating table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

#Insert some more records
cursor.execute('''Insert Into STUDENT values('Jacob','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Amit','Software Developer','B',100)''')
cursor.execute('''Insert Into STUDENT values('Rahul','Finance','A',80)''')
cursor.execute('''Insert Into STUDENT values('kirti','Marketing','B',94)''')
cursor.execute('''Insert Into STUDENT values('Aditi','Economics','C',90)''')
cursor.execute('''Insert Into STUDENT values('Ravi','Data Science','D',87)''')
cursor.execute('''Insert Into STUDENT values('Shivam','Marketing','B',60)''')
cursor.execute('''Insert Into STUDENT values('Aman','Software Developer','C',70)''')
cursor.execute('''Insert Into STUDENT values('Alok','Finance','B',78)''')
cursor.execute('''Insert Into STUDENT values('Simon','Data Science','A',88)''')
cursor.execute('''Insert Into STUDENT values('Ruby','Software Developer','D',98)''')
cursor.execute('''Insert Into STUDENT values('Mary','Data Science','C',100)''')
cursor.execute('''Insert Into STUDENT values('Raj','Finance','B',50)''')
cursor.execute('''Insert Into STUDENT values('Clara','Software Developer','A',64)''')
cursor.execute('''Insert Into STUDENT values('Esther','Data Science','C',91)''')
cursor.execute('''Insert Into STUDENT values('Allic','Software Developer','A',85)''')
cursor.execute('''Insert Into STUDENT values('Ruth','Finance','B',76)''')
cursor.execute('''Insert Into STUDENT values('Rose','Data Science','D',69)''')
cursor.execute('''Insert Into STUDENT values('Grace','Economics','A',90)''')
cursor.execute('''Insert Into STUDENT values('Nancy','Software Developer','D',91)''')
cursor.execute('''Insert Into STUDENT values('France','Finance','C',81)''')
cursor.execute('''Insert Into STUDENT values('Seema','Data Science','A',67)''')
cursor.execute('''Insert Into STUDENT values('Riya','Marketing','B',89)''')
cursor.execute('''Insert Into STUDENT values('Siya','Data Science','A',100)''')
cursor.execute('''Insert Into STUDENT values('Olivia','Economics','C',90)''')
cursor.execute('''Insert Into STUDENT values('James','Software Developer','D',80)''')
cursor.execute('''Insert Into STUDENT values('Emma','Data Science','B',78)''')
cursor.execute('''Insert Into STUDENT values('Vivek','Economics','C',56)''')
cursor.execute('''Insert Into STUDENT values('Sheetal','Marketing','A',45)''')
cursor.execute('''Insert Into STUDENT values('Satish','Data Science','B',83)''')
cursor.execute('''Insert Into STUDENT values('Jay','Software Developer','D',72)''')
cursor.execute('''Insert Into STUDENT values('Rohit','Data Science','A',52)''')
cursor.execute('''Insert Into STUDENT values('Dan','Economics','B',90)''')
cursor.execute('''Insert Into STUDENT values('David','Marketing','A',70)''')
cursor.execute('''Insert Into STUDENT values('Robert','Software Developer','C',60)''')

#Display all record
print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

#close the connection
connection.commit()
connection.close