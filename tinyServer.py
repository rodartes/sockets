#purpose: the purpose of tinyServer.py is to create a simple HTTP server

import socket

#1. set host and port variables for the server

myHost = '127.0.0.1'
myPort = 1025

#2. write the message to be sent to the client

message = "HTTP/1.1 200 OK\r\n"\
      "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
      "<html> Congratulations! You just downloaded your first Wireshark file! </html>\r\n"

#3. create and run socket - (referenced from https://docs.python.org/3/library/socket.html#example)

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((myHost, myPort))
mySocket.listen(1)
conn, addr = mySocket.accept()
with conn:
   print('Connected by:', addr)
   while True:
      data = conn.recv(1024)
      if not data: break
      conn.sendall(data)
      conn.sendall(message)
