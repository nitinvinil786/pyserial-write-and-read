#!/bin/python3
import serial
import time
import array as serialbytedata

serialdata = serialbytedata.array('B', [])
switch_count = 0

def clear_serial_data():
    global switch_count
    for i in serialdata: 
        serialdata.remove(i)		
    switch_count = 0	
	
serialobj = serial.Serial('/dev/ttyUSB0',9600)

if serialobj.isOpen():
    serialobj.close()
serialobj.open()
serialobj.isOpen() 

clear_serial_data()


while 1:
	while serialobj.in_waiting:
		rxd_data = int.from_bytes(serialobj.read(), "big")
		match switch_count:
			case 0:
				if rxd_data == 0x1A:					
					serialdata.insert(switch_count,rxd_data)
					switch_count += 1
				else:
					clear_serial_data()
			case 1:			
				if rxd_data == 0x03:
					serialdata.insert(switch_count,rxd_data)
					switch_count += 1
				else:
					clear_serial_data()	
			case 2:
				if rxd_data == 0x03:
					serialdata.insert(switch_count,rxd_data)
					switch_count += 1
				else:
					clear_serial_data()	
			case 3:
				if rxd_data == 0xE8:
					serialdata.insert(switch_count,rxd_data)
					switch_count += 1
				else:
					clear_serial_data()	
			case 4:
				if rxd_data == 0x00:
					serialdata.insert(switch_count,rxd_data)
					switch_count += 1
				else:
					clear_serial_data()	
			case 5:
				if rxd_data == 0x78:
					serialdata.insert(switch_count,rxd_data)
					switch_count += 1
				else:
					clear_serial_data()	
			case 6:
				if rxd_data == 0xC6:
					serialdata.insert(switch_count,rxd_data)
					switch_count += 1
				else:
					clear_serial_data()			
			case 7:
				if rxd_data == 0x73:					
					serialdata.insert(switch_count,rxd_data)
					print(serialdata)
					clear_serial_data()
				else:
					clear_serial_data()					
	
serialobj.close()
