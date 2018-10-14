import sys, string
import time
import random
import math
from copy import copy, deepcopy

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def validn(kit,P,n):
    for i in range(len(kit)):
        if kit[i] < P[i]*n*0.9:
            #~ print "ovf", kit[i], P[i], P[i]*n*0.9
            return None
        if kit[i] > P[i]*n*1.1:
            #~ print "nai", kit[i], P[i], P[i]*n*1.1
            return False

    return True

# 0 = overflow
def valid(kit,P):
    #~ print kit,P
    nmin = min([math.ceil(kit[i] / (P[i] * 1.1)) for i in range(len(P))])
    nmax = max([math.floor(kit[i] / (P[i] * 0.9)) for i in range(len(P))])
    #~ return nmax >= nmin
    
    for n in range(int(nmin), int(nmax+1)):
    #~ while 1:
        #~ n += 1
        #~ print n
        v = validn(kit,P,n)
        #~ print v, v==0
        if v:
            return n
        if v == None:
            return 0
    # unreachable

def solve(N,P,M):
    #~ print R
    #~ print M
    #~ print P
    #~ print valid([M[0][0], M[1][0]], P)
    #~ print valid([1500,809], [500,300])
    ans = 0
    if N == 1:
        assert len(M) == N
        assert len(P) == N
        for i in range(len(M[0])):
            #~ print M[0][i], P
            if valid([M[0][i]], P):
                #~ print "v"
                ans += 1
    elif N == 2:
        best = 0
        M0 = M
        for k in range(100):
            M = deepcopy(M0)
            #~ print M
            ans = 0
            ri = range(len(M[0]))
            rj = range(len(M[1]))
            random.shuffle(ri)
            random.shuffle(rj)
            for i in ri:
                for j in rj:
                    if M[0][i] and M[1][j]:
                        v = valid([M[0][i], M[1][j]], P)
                        if v:
                            #~ print M[0][i], M[1][j], v
                            ans += 1
                            M[0][i] = 0
                            M[1][j] = 0
            best = max(best, ans)
        ans = best
            
        pass
    else:
        print N
        assert 0
    return ans        

T = readint()
for t in range(T):
    N,P = readlist()
    R = readlist()
    assert len(R) == N
    M = []
    for i in range(N):
        M.append(readlist())
        assert len(M[-1]) == P

    #~ if t+1 != 93:
        #~ continue

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    print solve(N,R,M)
