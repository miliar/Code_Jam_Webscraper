import sys, string
from copy import copy, deepcopy
import gmpy
import time

import sys
sys.setrecursionlimit(1000000)

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readbinlist():
	return [int(x,2) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

T = readint()

for t in range(T):
    Smax, S = sys.stdin.readline().strip().split(" ")
    Smax = int(Smax)
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    #print S
    
    extras = 0
    standing = 0
    for i in range(Smax+1):
        shy = int(S[i])
        if standing >= i:
            standing += shy
        elif shy:
            extras += (i - standing)
            standing += shy + extras
    print extras
