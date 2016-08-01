#!/usr/bin/env python

# Auralius Manurung, 2016
# manurung.auralius@gmail.com

import socket
import struct
import sys, getopt

UDP_IP = "127.0.0.1"
UDP_PORT = 12345

def printinfo():
	print '===================================================================='
	print 'send_doubles.py -i <remote ip> -p <remote port>'
	print 'If not defined, IP address is ', UDP_IP, ' and the port is ', UDP_PORT
	print 'Example: send_doubles.py -i "127.0.0.1" -p 12345'
	print '===================================================================='
	return

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hi:p:",["ip=","port="])
	except getopt.GetoptError:
		printinfo()
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			printinfo()
			sys.exit()
		elif opt in ("-i", "--ip"):
			UDP_IP = arg
		elif opt in ("-p", "--port"):
			UDP_PORT = int(arg)

	print 'Remote IP: ', UDP_IP
	print 'Remote port: ', UDP_PORT
	print '===================================================================='
	s = raw_input("Enter the array of double, separated by space: ")

	# Handle excessive spaces and convert to double
	s = s.split(' ')
	s = [x.replace(' ', '') for x in s]
	s = filter(lambda name: name.strip(), s)
	s = map(float, s)

	print s

	# Pack and send
	n = len(s);
	data = ""
	for i in range(0, n):
		data += struct.pack("d", s[i])	

	sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
	sock.sendto(data,(UDP_IP, UDP_PORT))

if __name__ == "__main__":
	main(sys.argv[1:])