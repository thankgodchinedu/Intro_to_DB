import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',      # MySQL server host
        user='root',           # Your MySQL username
        password='your_password'  # Your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor.is_connected():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
