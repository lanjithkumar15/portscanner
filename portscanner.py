import nmap
import socket
import time
import datetime
import os
os.system('clear')
from datetime import datetime
print("DATE AND TIME NOW : ",datetime.utcnow())
nm = nmap.PortScanner()
print("NMAP VERSION YOU USING ",nm.nmap_version(),"\n")
x = input("ENTER THE HOST NAME : ")
ip = socket.gethostbyname(x)
print("IP ADDRESS : ",ip)
y = input("ENTER THE START RANGE  TO END RANGE OF PORT EX: (1-400))1(start)-1(end below(65535)) : ")
print("LIKE EXAMPLES:\n-sU - UDP SCAN \n-sO - IP protocol scan\n-O-Enable OS detection\n-sV is default etc.,,")
z= input("ENTER THE SWITCH YOU WANT TO USE (EG:-sC ): ")
g = int(input("ENTER THE 1(root) or (0)(non-root) : "))
if g==1:
    g = True
else:
    g=False
print("SCAN STARTED ")
print("OUTPUT FORMAT : HOST; HOSTNAME; HOSTNAME_TYPE; PROTOCOL; PORT; NAME; STATE; PRODUCT; EXTRAINFO; REASON; VERSION; CONF; CPE ")
print("-" * 100)
nm.scan(x,y,z,g)
filename = input("ENTER THE FILE NAME TO SAVE THE OUTPUT : ")
f = open(filename, "w")
f.write(nm.csv())
print("WRITED SUCCESSFULLY ")
print("_" * 100)
print("PRINTING THE SCAN RESULT")
time.sleep(3)
f = open(filename, "r")
for i in f:
    print(i) 
print("_ " * 100,"\n")
print("SCANNED SUCCESSFULLY \n")
print("THANK YOU!!!!! \n")
print("-" * 100)