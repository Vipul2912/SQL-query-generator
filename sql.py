import sqlite3

##  connect to sqlite
connection = sqlite3.connect("student.db")

## creaate a cursor object to insert record , create table, retrieve

cursor = connection.cursor()

# create the table

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

# insert some more records

cursor.execute('''Insert Into STUDENT values('Vipul','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sahil','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Nitesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikrant','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Sidhu','DEVOPS','A',35)''')

# Display all the records

print("The inserted records are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
  print(row)

#close the connection
  
connection.commit()
connection.close()
