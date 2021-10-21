import socket
import sys
import time


s=socket.socket()
host=input(str("please enter the host name of the server:"))
port=8080
s.connect((host,port))
s.close()
print("connected to chat server")
while 1:
    incomming_message=s.recv(1024)
    incomming_message=incomming_message.decode()
    print("")
    print("server:",incomming_message)
    message=input(str(">>"))
    message=message.encode()
    s.send(message)
    print("message has been sent..")
    print("")
