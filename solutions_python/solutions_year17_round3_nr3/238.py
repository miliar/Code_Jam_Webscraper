from collections import Counter
from heapq import heappush, heappop
def f():
    tc, = map(int, raw_input().split())
    for _tc in xrange(tc):
        N, K = map(int, raw_input().split())
        U, = map(float, raw_input().split())
        P = map(float, raw_input().split())
        #print N, K, U, P, 
        c = Counter(P)
        c[1.0] += 0
        q = []
        for x in c.items(): heappush(q, x)
        p, c = heappop(q)
        #print p, c, U, q
        while U and q:
            np, nc = heappop(q)
            dist = (np-p)*c
            if dist > U:
                dist = U
                p, c = p + dist/c, c
                heappush(q, (np,nc))
                U = 0
            else:
                p, c = p + dist/c, c+nc
                U = U-dist
            #print p, c, U, q
        res =  p**c
        while q:
            np, nc = heappop(q)
            res *= np**nc
        print 'Case #%d: %0.6f' % (_tc+1, res)
f()

