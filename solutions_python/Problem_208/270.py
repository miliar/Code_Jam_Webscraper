import sys, string
import time
import random
import math
from copy import copy, deepcopy

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def solve(M):
    return 0

T = readint()
for t in range(T):
    N, Q = readlist()
    
    E = []
    S = []
    for i in range(N):
        e,s = readlist()
        E.append(e)
        S.append(s)

    D = []
    for i in range(N):
        d = readlist()
        if i < N-1:
            d = d[i+1]
            D.append(d)

    for i in range(Q):
        U,V = readlist()
        assert U == 1
        assert V == N
    
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),

    print >> sys.stderr, N, Q, E, S, D
    dend = 0


    tbest = [float("inf")]*N
    dcums = [float("inf")]*N
    tbest[N-1] = 0
    dcums[0] = 0

    dacc = 0
    for i in range(N-1):
        dacc += D[i]
        dcums[i+1] = dacc
    #~ print dcums

    for i in range(N-2, -1, -1):
        print >> sys.stderr, i
        e, s, d = E[i], S[i], D[i]
        dend += d
        print >> sys.stderr, e, s, d
        # can we take this horse?
        tbl = 1e1000
        for j in range(i+1,N):
            dij = dcums[j]-dcums[i]
            print >> sys.stderr, "(%d->%d) d=%d" % (i+1,j+1,dij)
            if e >= dij:
                # yes!
                tl = 1.0 * dij / s + tbest[j]
                print >> sys.stderr, "   ", j, dij, tl, 1.0 * dij / s, tbest[j]
                tbl = min(tbl, tl)
        tbest[i] = tbl

    print >> sys.stderr, tbest
    print >> sys.stderr, dcums
    print "%.9f" % tbest[0]
