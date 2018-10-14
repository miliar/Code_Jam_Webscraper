#from __future__ import division
import sys, string
import itertools
from math import *

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

def shl(x,n):
    s = str(x)
    s = s[n:] + s[:n]
    return int(s)

def recycled(a,b):
    n = len(str(a))
    for i in range(n):
        if b == shl(a,i):
           return 1
    return 0

def num_recycled(A,B):
    n = 0
    for i in range(A,B):
        for j in range(i+1, B+1):
            if recycled(i,j):
                n += 1;
    return n

for k in range(T):
    A,B = readlist()
    print >> sys.stderr, k
    print "Case #%d: %d" % (k+1, num_recycled(A,B))
