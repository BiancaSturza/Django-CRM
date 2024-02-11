import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'expozitiunea123',
	auth_plugin = 'mysql_native_password',

	)

#prepare a cursor object

cursorObject = dataBase.cursor()

#Create the database

cursorObject.execute("CREATE DATABASE mydatabase")
print("All Done!")
