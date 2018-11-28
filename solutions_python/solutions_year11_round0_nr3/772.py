#!/usr/bin/python

# google code jam - c.durr - 2011

# CandySplitting
# - ad-hoc, temps lineaire

try:
    import psyco
except:
    pass

from math import *

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

for test in range(readint()):
    N = readint()
    L = readarray(int)
    a = reduce(lambda x,y: x+y,      L)
    b = reduce(lambda x,y: x^y,      L)
    c = reduce(lambda x,y: min(x,y), L)
    if b!=0:
        print "Case #%i: NO"% (test+1)
    else:
        print "Case #%i:"% (test+1), a-c

    
    
