#!/usr/bin/python
from __future__ import print_function
from sys import stdin

def readiline():
    return map( int, stdin.readline().strip().split() )

def readsline():
    return map( str, stdin.readline().strip().split() )

T, = readiline()

for i in xrange(1,T+1):
    currAudience = 0
    needed = 0
    Smax, audience = readsline()
    Smax = int(Smax)
    for currShyness in range(0, Smax+1):
        if currAudience >= currShyness:
            currAudience += int(audience[currShyness])
        else:
            needed += currShyness - currAudience
            currAudience = currShyness + int(audience[currShyness])
    
    print ('Case #%d: %d' % (i, needed))
