
from collections import deque
import math
import sys

from heapq import heappush, heappop


def div(v):
    i = v//2
    if 2*i==v: return (i, i)
    return (i, i+1)


def simulate(N, K):
    q = []
    heappush(q, (-N, 1))
    while True:
        N, cnt = heappop(q)
        N = -N
        K -= cnt
        mn, mx = div(N-1)
        if K<=0: break
        
        if mn==mx and mn>0:
            heappush(q,  (-mn,2*cnt) )
        else:
            if mn>0: heappush(q,  (-mn,cnt) )
            if mx>0: heappush(q,  (-mx,cnt) )

    return mx, mn



fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

T = int(fin.readline())

for t in range(T):
    l = fin.readline()
    N = int(l.split()[0])
    K = int(l.split()[1])
    mx, mn = simulate(N, K)
    fout.write("Case #%i: %i %i\n" % (t+1, mx, mn))

