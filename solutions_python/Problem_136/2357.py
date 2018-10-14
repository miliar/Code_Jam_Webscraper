#!/usr/bin/python 

from __future__ import division

def cookieClicker (C, farm_rate, X):
    rate = 2
    total_time=0
    while True:
        if C/rate + X/(rate + farm_rate) < X/rate:
            total_time = total_time +  C / rate
            rate = rate + farm_rate
        else:
            total_time = total_time + X/rate
            break
    return total_time

name='input'
fp_in = open (name, "r")
fp_out = open ('output.txt', "w")
lines = fp_in.readlines ()
no_of_lines = int (lines [0])
print "test cases need to be read ", no_of_lines
lines = lines [1:no_of_lines+1]

output = 1
for input in lines:
    values = input.split ()
    print values
    time = cookieClicker (float (values [0]), float (values [1]), float (values [2]))
    fp_out.write ("case #" + str(output) +": " + str (time))
    fp_out.write ("\n")
    output = output + 1

fp_in.close ()
fp_out.close ()
    



