import sys, string
from copy import copy, deepcopy
import gmpy
import time

import sys
sys.setrecursionlimit(1000000)

def readlist():
	return [float(x) for x in sys.stdin.readline().strip().split(" ")]

def readbinlist():
	return [int(x,2) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

T = readint()

for t in range(T):
    N, V, X = readlist()
    R = []
    C = []
    for i in range(N):
        r,c = readlist()
        R.append(r)
        C.append(c)
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    
    #~ print N, V, X, R, C
    if N == 2 and C[0] == C[1]:
        N = 1
        R[0] += R[1]

    if N == 1:
        if C[0] == X:
            print "%.9f" % (V / R[0])
        else:
            print "IMPOSSIBLE"
    if N == 2:
        v0 = V*(C[1]-X)/(C[1]-C[0])
        v1 = V*(X-C[0])/(C[1]-C[0])
        #~ print v0,v1
        if v0 < -1e-7 or v1 < -1e-7:
            print "IMPOSSIBLE"
            continue
        t0 = v0 / R[0]
        t1 = v1 / R[1]
        #~ print t0, t1
        print "%.9f" % max(t0, t1)
