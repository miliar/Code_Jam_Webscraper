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

def calc(RH):
    A = 0
    N = len(RH)
    pi = math.pi
    lastr = 0
    for i in range(N):
        r,h = RH[i]
        #~ print >> sys.stderr, r, lastr, h
        A += pi * r * r - pi * lastr * lastr + 2 * pi * r * h
        lastr = r
    return A

T = readint()
for t in range(T):
    N, K = readlist()
    RH = []
    for i in range(N):
        r, h = readlist()
        RH.append((r,h))
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),

    RH.sort(key=lambda x: x[0])
    #~ print RH
    #~ print calc(RH)
    best = 0
    for b in range(1 << N):
        RHs = []
        for i in range(N):
            if b & (1 << i):
                RHs.append(RH[i])
        if len(RHs) == K:
            print >> sys.stderr, RHs, calc(RHs)
            c = calc(RHs)
            best = max(best, c)
    print "%.9f" % best
