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
    D, N = readlist()
    
    K = []
    S = []
    for i in range(N):
        k,s = readlist()
        K.append(k)
        S.append(s)

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),

    #~ print >> sys.stderr, D, N, K, S
    tmin = 0
    for i in range(N):
        t = (1.0 * D - K[i]) / S[i]
        tmin = max(tmin, t)
    #~ print >> sys.stderr, tmin
    print "%.06f" % (1.0 * D / tmin)
