import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dbms1234'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE sfbs")
print("All done!!")