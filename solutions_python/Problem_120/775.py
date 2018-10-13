#!/usr/bin/python

import sys
import math

if len(sys.argv) != 2:
    print "Please pass command Line argument to run the program: python file.py inputFilename"
    sys.exit()

try:
    f = open(sys.argv[1],'r')
    count = int(f.readline())
except IOError:
    print "Input File Could not be opened"
    sys.exit()

i = 1

case = 1

while True:
    line = f.readline();
    if not line:
        f.close()
        break
    line.rstrip()
    vals = line.split()
    r = int(vals[0])
    t = int(vals[1])

    #print r
    #print t

    count = 0
    r = r + 1

    while t > 0:
        val = (r * r) - ((r - 1) * (r - 1))
        r = r + 2
        if val <= t:
            #print count
            count = count + 1
            t = t - val
        else:
            break


        
    print "Case #" + str(case) + ": " + str(count)
    case = case + 1
    
