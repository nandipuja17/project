import socket
import sys
import time

##end of import###
###init ###

s=socket.socket()
host=socket.gethostname()
print ('server will start on host:',host)
port=8080
s.bind((host,port))
print("")
print("server done binding to host and port successfully")
print("")
print("server is wating for incomming connection")
s.listen()
conn,addr=s.accept()
print(addr,"has connected to the server and is now online..")
print("")
while 1:
    message=input(str(">>"))
    message=message.encode()
    conn.send(message)
    print("message has been sent..")
    print("")
    incomming_message=conn.recv(1024)
    incomming_message=incomming_message.decode()
    print("")
    print("client:",incomming_message)
