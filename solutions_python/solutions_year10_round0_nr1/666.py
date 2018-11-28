#!/usr/bin/python
import sys
import snap
import math

if len(sys.argv) < 2:
    print "usage: "+sys.argv[0]+" inputfile"
    sys.exit (0)

file = open (sys.argv[1], "r");

chunk = file.readline ();
lines =  int (chunk)
ii = 0
while (ii < lines):
    chunk = file.readline ();
    chunk = chunk.strip()
    csp = chunk.split(" ")
    n = int(csp[0])
    k = int(csp[1])
    period = math.pow(2,n)
    mod = k%period;
    ii = ii + 1
    if (mod == (period - 1)):
        print "Case #"+str(ii)+": ON";
    else:
        print "Case #"+str(ii)+": OFF";


