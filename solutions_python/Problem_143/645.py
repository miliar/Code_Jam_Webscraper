
from serial import Serial, EIGHTBITS, STOPBITS_ONE

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = Serial(
    port='COM4',
     baudrate=2400, bytesize=EIGHTBITS,  stopbits=STOPBITS_ONE)

ser.isOpen()
while 1 :
    
    out = ''
    while ser.inWaiting() > 0:
        out += ser.readline()
        print out
        