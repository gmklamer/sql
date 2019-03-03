# Python 3
import sqlite3

# Function to create a database
def createdb():
	fconn = sqlite3.connect('student.db')
	cursor = fconn.cursor()
	sql = '''create table students (
		name text,
		username text,
		id int)'''
	try:
		cursor.execute(sql)
		cursor.close()
	except:
		pass
	
createdb()
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
print ("Let's input some students!")
while True:
	name = input('Student\'s name: ')
	username = input('Student\'s username: ')
	id_num = input('Student\'s id: ')
	sql = ''' insert into students
		(name, username, id)
		values
			(:st_name, :st_username, :id_num)'''
	cursor.execute(sql, {'st_name':name, 'st_username':username, 'id_num':id_num})
	conn.commit()
	cont = input("Another student? ")
	if cont[0].lower() == 'n':
		break	
cursor.close()
print ("All done. Bye now")