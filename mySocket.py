#purpose: the purpose of mySocket.py is to GET a file from a server

import socket

#1. Make variables for host, GET request, and port number (port 80 for HTML)

myHost = 'gaia.cs.umass.edu'
myRequest = 'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
myPort = 80

#2. connect host and port to listen for a message - (referenced from: https://realpython.com/python-sockets/)

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((myHost, myPort))
mySocket.sendall(myRequest.encode())
data = mySocket.recv(1024).decode()

#3. close socket and print the server's response

mySocket.close()
print('[RECV]-', repr(data))
