# Software-Engineering-1-MS
Microservice implementation for my partners CS361 project

This is a microservice which, when connected to, queries a database for the top ten most 'liked' locations in a database holding tourist attractions.
To request data from this microservice all one has to do is run the microservice program and connect to the host and port that the microservice is listening on.
    the host is 127.0.0.1 and the port is 6060.
When one connects to that host and port via any method they choose, the microservice will connect to a database that has to be set up and specified in the server.py file,
    query the database, turn the results into a string, and send that string over the connection made it it. 
In order to specify a data base one has to change the variables 'host', 'user', 'password', 'database' in the server.py file.
The client will be sent the data automatically, as stated above, but into to use is after its receipt the client will have to be able to use a socket recieve function.
    for example, in the simple client.py file I connected to the host my server was listening on using a socket. Then I called the s.recieve function and set that equal to
    a variable which can then be used at any time in my client.
    ```
    host = "127.0.0.1"  # The server's hostname or IP address
    port = 6060  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        message = s.recv(1024)

    ```
Above is an example of how we can connect/request to the server and recieve from the server. We connect using a socket on the specific host and port and then set the variable
    'message' equal to our socket.recv() or s.recv() The server does all the rest of the work automatically on the back end and returns the top ten places in the database.


    -------------UML Sequence Diagram------------------------
    ![UML sequence diagram](https://app.diagrams.net/)