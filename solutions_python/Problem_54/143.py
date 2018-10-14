#!/bin/python

import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

inf = sys.stdin
C = int(inf.readline())
    
for c in range(C):
    times = map(int, inf.readline().split())[1:]
    #print 'times', times
    
    # sort times, take successive diffs
    # get gcd of diffs, then find when it next occrs
    times.sort()
    #print 'sorted', times
        
    diffs = [times[i] - times[i-1] for i in range(1, len(times))]
    #print 'diffs', diffs
    
    diffs.sort()
    #print 'sorted diffs', diffs
    # remove zeros
    while len(diffs) > 0 and diffs[0] == 0:
        diffs = diffs[1:]
        
    if len(diffs) == 0:
        T = 1
    elif len(diffs) == 1:
        T = diffs[0]
    else:
        T = reduce(gcd, diffs)
    
    #print 'T', T
    # next time when times are divisible by T:
    result = times[0] % T
    if result > 0:
        result = T - result
    
    print 'Case #%d: %s' % (c+1, result)