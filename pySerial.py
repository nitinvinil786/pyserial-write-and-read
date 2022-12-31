#!/bin/python3
import serial
import time
serialobj = serial.Serial('/dev/ttyUSB1',9600)
if serialobj.isOpen():
    serialobj.close()
serialobj.open()
serialobj.isOpen() 
serialobj.timeout = 3
serialobj.write('hello\n'.encode())   # or serialobj.write(b'hello\n')
ReceivedString = serialobj.readline()
print(ReceivedString)
serialobj.close()
