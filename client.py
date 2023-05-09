#!/usr/bin/env python3

import socket

host = "127.0.0.1"  # The server's hostname or IP address
port = 6060  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    message = s.recv(1024)

print(f"Received message: {message}")