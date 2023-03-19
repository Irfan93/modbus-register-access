# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import datetime
from datetime import datetime
import time
import csv
from time import strftime
import os

os.chdir('C:/Users\mkajanajumudeen/OneDrive - NIBE AB/Desktop/tempdatalogs')

row = ['DateTime', 'iGate', 'Ecobee']

filename = strftime("%a_%d-%b-%Y_%H-%M-%S")

f = open(filename+".csv", 'w')
writer = csv.writer(f)
writer.writerow(row)

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM7',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()
request = b'\x10\x03\x51\xEA\x00\x01\xB6\x43'

ser1 = serial.Serial(
    port='COM8',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)

ser1.isOpen()
request = b'\x10\x03\x51\xEA\x00\x01\xB6\x43'

try:
    while True:
        time.sleep(5)
        ser.write(request)
        buf = '' 
        time.sleep(1) 
    
        while ser.inWaiting() > 0: 
            buf+=str(ser.read(1)) 
        
        indoor_temp_iGate = int(buf[25:27]+buf[32:34], 16)/10
        
        ser1.write(request)
        buf1 = '' 
        time.sleep(1) 
    
        while ser1.inWaiting() > 0: 
            buf1+=str(ser1.read(1)) 
        
        indoor_temp_ecobee = int(buf1[25:27]+buf1[32:34], 16)/10
    
        #logging data
        data = [time.strftime("%a, %d %b %Y %H:%M:%S"), indoor_temp_iGate, indoor_temp_ecobee ]
        writer.writerow(data)
except KeyboardInterrupt:
    f.close()
    print('data logging ended')
    ser.close()
    ser1.close()
    print("Ports are closed")
