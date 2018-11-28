from __future__ import division
import sys, string
import itertools
from math import *

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

def pal(x):
    return str(x) == str(x)[::-1]

for k in range(T):
    print >> sys.stderr, k
    a,b = readlist()
    
    c = 0
    for x in range(int(sqrt(b))+1):
        xs = x*x
        if pal(x) and pal(xs):
            if xs >= a and xs <= b:
                print >> sys.stderr, x, x*x
                c += 1

    ans = c
    print "Case #%d: %s" % ((k+1), ans)
