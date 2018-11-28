#from __future__ import division
import sys

rl = lambda: sys.stdin.readline().strip()

def getA(n):
    if n==0:
        return [0, 0]
    if n%3==0:
        if n==3:
            return [1, 1]
        else:
            return [n/3, n/3+1]
    if n%3==1:
        if n==1:
            return [1, 1]
        else:
            return [(n-1)/3+1, (n-4)/3+2]
    if n%3==2:
        if n==2:
            return [1, 2]
        else:
            return [(n-2)/3+1, (n-2)/3+2]

for c in range(int(rl())):
    v = map(int, rl().split())
    N = v[0]
    S = v[1]
    P = v[2]
    T = v[3:]
    
    ans = 0
    for t in T:
        A = getA(t)
        #print t, A, P
        if A[0]>=P:
            ans += 1
        elif A[1]>=P and S>0:
            S -= 1
            ans += 1
        
    print 'Case #%d: %d' % (c+1, ans)