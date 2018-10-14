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

def expand(S):
    m, p = S
    
    yield (m+1, [max(x-1,0) for x in p])
    
    M = max(p)
    for i in range(len(p)):
        if p[i] == M:
            for j in range(len(p)+1):
                if i != j:
                    for k in range(p[i]/2-1, p[i]/2+2):
                    #~ for k in [p[i]/2, (p[i]+1)/2]:
                        if k >= 2:
                            #~ k = p[i]/2
                            #~ print >> sys.stderr, i, j, k
                            pc = copy(p)
                            if j == len(pc): pc.append(0)
                            pc[i] -= k
                            pc[j] += k
                            if pc[j] <= M - 1:
                                yield (m+1, sorted(pc))

for t in range(T):
    D = readint()
    P = readlist()
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),

    P = sorted(P)
    s = (0,P)
    Q = [s]
    best = max(P)
    
    i = 0
    while i < len(Q):
        s = Q[i]
        for c in expand(s):
            if c not in Q:
                if c[0] >= best:
                    continue

                if max(c[1]) == 0:
                    print >> sys.stderr, c
                    best = min(best, c[0])
                    continue

                worst_case = c[0] + max(c[1])
                if worst_case < best:
                    print >> sys.stderr, worst_case, c
                    best = worst_case
                
                #~ print >> sys.stderr, c
                Q.append(c)
        i += 1
    print best
