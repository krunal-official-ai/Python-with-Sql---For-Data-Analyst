import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    password='********',
    user='root'
)

if conn.is_connected():
    print("Connection established...")
