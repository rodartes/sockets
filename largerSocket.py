#purpose: the purpose of largerSocket.py is to GET a file of a large size

import socket
#import sys

#1. Make variables for host, GET request, and port number

myHost = 'gaia.cs.umass.edu'
myRequest = 'GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
myPort = 80

#2. connect host and port to listen for a message until bytes read is <=0

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((myHost, myPort))
mySocket.send(myRequest.encode())

response = ''
size = 1

while size > 0:
   data = mySocket.recv(1024)
   size = len(data.decode())
   response = response + data.decode()

mySocket.close()
print('[RECV]-', response)

