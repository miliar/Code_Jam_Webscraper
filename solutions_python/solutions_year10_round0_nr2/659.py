#!/usr/bin/python2.6

from numpy import diff
import fractions

def findY(events):
    events = sorted(events)
    deltas = diff(events)
    gcd = deltas[0]
    for i in range(1,len(deltas)):
        gcd = fractions.gcd(gcd,deltas[i])
    
    first = min(events)
    
    newFirst = (first/gcd)
    newFirst = newFirst * gcd
    if(newFirst<first):
        newFirst = newFirst + gcd
    
    return newFirst - first    
    

c = input()

for i in range(c):
    ri = raw_input().split()
    events = map(long,ri[1:])
    y = findY(events)
    print "Case #%d: %d" % (i+1, y)





    
    
