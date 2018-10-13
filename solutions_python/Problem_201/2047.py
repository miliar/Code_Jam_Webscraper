import sys, string
import time
import random
from collections import defaultdict
import math

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def sol(N):
    if N == 0: return 0,0
    return (N/2,N/2) if N % 2 else (N/2,N/2-1)

def solve(N, K):
    Q = [N]

    while K:
        N = Q[0]
        Q = Q[1:]
        if N % 2:
            Q.append(N/2)
            Q.append(N/2)
        else:
            Q.append(N/2)
            Q.append(N/2-1)
        Q.sort(reverse=True)
        #~ print Q

        K -= 1

    return N
    return sol(N)

def solveD(N, K):
    Q = defaultdict(int)
    Q[N] += 1

    while K:
        N = max(Q.keys())
        Q[N] -= 1
        if Q[N] == 0:
            del Q[N]
        
        #~ print N
        if N % 2:
            Q[N/2] += 1
            Q[N/2] += 1
        else:
            Q[N/2] += 1
            Q[N/2-1] += 1
        #~ print Q

        K -= 1

    #~ return sol(N)    
    return N

def xsolve(N,K):
    ff = 2**int(math.log(N+1,2))-1
    off = N-ff
    num = 1
    while K > 0:
        N = (N-1) / 2.
        num *= 2
        K -= num
    K += num

    #~ return N, K*1.0/num
    return int(N)+1 if K*1.0/num <= N-int(N) else int(N)

def ysolve(N,K):
    if K == 0:
        return solve(N,K)
    return xsolve(N,K-1)

T = readint()
for t in range(T):
    N, K = readlist()

    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    s = sol(ysolve(N, K))
    print s[0], s[1]

    continue
    N=77
    print
    for i in range(1,N):
        print solve(N,i),
    print
    for i in range(1,N):
        print ysolve(N,i),
    #~ print xsolve(34,)
    #~ print xsolve(100001,7), solve(100001,7)
