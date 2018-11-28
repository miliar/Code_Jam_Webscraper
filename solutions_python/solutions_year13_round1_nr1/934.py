#!/usr/bin/env python


import sys
import math
from math import pi
T = int(input())

def check(r, t,  case):
    #print "Case", case
    c = 0
    i = 0
    total = t
    while True:
        c += pow(r+i+1, 2) - pow(r+i, 2)
        #print "pow(", r, "+", i+1 , ") pow(", r, "+" ,i, ")" , pow(r+i+1, 2) - pow(r+i, 2)
        i += 2
        if c > t:
            i -= 2
            break
        if c == t:
            break
        
   
    print "Case #%d: %d" % (case+1, i/2)
   
    


for i in range(T):
    line = raw_input().split()
    r, t = int(line[0]), int(line[1])
    check(r, t, i)

#for line in sys.stdin:
#    print line.strip()
    
