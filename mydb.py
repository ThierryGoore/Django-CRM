import mysql.connector 

DATABASE = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'Thiesco56777@79',

 )



#prepare a cursor object 
cursorObject = DATABASE.cursor()
#create a database
cursorObject.execute("CREATE DATABASE finalElderco")

print("All done!")
