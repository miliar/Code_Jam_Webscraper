#!/usr/bin/python
import sys

def findMax(params):
    N = params[0] #number of dancers
    S = params[1] #number of surprising results
    p = params[2] #threshold for counting
    dancers = params[3:]
    count = 0
    for x in dancers:
        if x>=3*p-2: #at least (p-1,p-1,p)
            count=count+1 
        elif x>=3*p-4 and S>0 and p>1: # (p-2,p-1,p) or (p-2,p-2,p)
            count=count+1
            S=S-1
    return count

T = int(sys.stdin.readline())
for i in xrange(T):
    params = [int(x) for x in sys.stdin.readline().split()]
    print 'Case #%d: %d' % (i+1,findMax(params))
