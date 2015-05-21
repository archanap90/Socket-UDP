#UDPPingerClient.py
from socket import *
from datetime import datetime
import time

    
#Create a UDP Client Socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

host = '127.0.0.1'
port = 12001

seqNumber = 1 
while(seqNumber <= 10):
     pingMsg = "Ping " + str(seqNumber) + " " + str(datetime.now())
    
     #Ping Server and start the timer
     tmrStart = time.time()
     print pingMsg
     clientSocket.sendto(pingMsg,(host, port))
     #Set the timeout to 1second
     clientSocket.settimeout(1)

     try:
          #Receive response from the server	
          respMsg = clientSocket.recvfrom(1024)

          tmrEnd = time.time()
     
          reply = respMsg[0]
          addr = respMsg[1]

          print "Server response: "+ str(reply)
          print "RTT" + str(seqNumber) + " = " + str(tmrEnd-tmrStart) + " seconds\n"
     
     except:
          print "Request timed out!!!\n"

     seqNumber+= 1

print "\nThe End!! Client Socket is closed."
clientSocket.close()
