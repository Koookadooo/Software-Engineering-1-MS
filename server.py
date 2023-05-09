
import socket
import mysql.connector
import time

host = "127.0.0.1"  # The server's hostname or IP address
port = 6060  # The port used by the server
HEADERSIZE = 20

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    connection, address = s.accept()
    with connection:
        print(f"Connected by {address}")

        time.sleep(3)
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="python_SW1_db",
            password="sw361",
            database="python_sw1_db"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT name FROM places ORDER BY likes LIMIT 10")
        myresult = mycursor.fetchall()
        print("Results from database query:", myresult)

        time.sleep(3)

        message=''
        for x in myresult:
            message += str(x) 
        
        print("Sending results to client ->")
    
        connection.send(bytes(str(message),"utf-8"))

    connection.close()