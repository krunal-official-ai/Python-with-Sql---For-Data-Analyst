import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    password='RKit_007',
    user='root'
)

if conn.is_connected():
    print("Connection established...")
