#!/usr/bin/env python

# Auralius Manurung, 2016
# manurung.auralius@gmail.com

import socket
import struct
import sys

UDP_IP = "127.0.0.1"

if len(sys.argv) < 2:
	UDP_PORT = 5008
else:
	UDP_PORT = int(sys.argv[1]);

print "===================================================================="
print "A UDP receiver for data in arrays of double"
print "Listening in port ", UDP_PORT
print "Send to this port the arrays of double to be displayed on the screen"
print "Ctrl+c to quit"
print "===================================================================="

sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
sock.bind( (UDP_IP,UDP_PORT) )

s = ""

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "Byte Length of Message :", len(data) ,"\n"
    
    s = ""
    for i in range(0, len(data)/8):
        s += "d"
    
    print "Message Data :", struct.unpack(s,data) ,"\n"