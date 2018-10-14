#!/usr/bin/env python
import sys
import re

_schedRE = re.compile(r'(\d\d):(\d\d)\s+(\d\d):(\d\d)')
_T = None

 # copy and paste is lame :(
 
def sortBintoA(x):
    global _T
    if 'A' == x[2]:
        return x[0]
    else:
        return x[1]+_T-.1
    
def sortAintoB(x):
    global _T
    if 'B' == x[2]:
        return x[0]
    else:
        return x[1]+_T-.1
    
for test in range(int(sys.stdin.readline())):
    trains =[]
    _T = int(sys.stdin.readline())
    A=0
    B=0
    NA,NB =[int(i) for i in sys.stdin.readline().split()]
    
    for _ in range(NA):
        m = _schedRE.match(sys.stdin.readline())
        trains.append((int(m.group(1))*60 +int(m.group(2)),
                       int(m.group(3))*60 +int(m.group(4)),
                       'A'
                       ))
    for _ in range(NB):
        m = _schedRE.match(sys.stdin.readline())
        trains.append((int(m.group(1))*60 +int(m.group(2)),
                       int(m.group(3))*60 +int(m.group(4)),
                       'B'
                       ))
        
    trains.sort(key=sortBintoA)
    fromB = 0
    for train in trains:
        if 'B' == train[2]:
            fromB += 1
            continue
        if fromB > 0:
            fromB -= 1
        else:
            A += 1
            
    trains.sort(key=sortAintoB)
    fromA = 0
    for train in trains:
        if 'A' == train[2]:
            fromA += 1
            continue
        if fromA > 0:
            fromA -= 1
        else:
            B += 1
    print "Case #%i: %i %i" %(test+1,A,B)
    