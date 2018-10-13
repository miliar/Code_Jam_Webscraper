from math import pi
from heapq import heappush, heappop
def f():
    tc, = map(int, raw_input().split())
    for _tc in xrange(tc):
        N, K = map(int, raw_input().split())
        pan = [None]*N
        q = []
        for i in xrange(N): 
            ri, hi = map(int, raw_input().split())
            pan[i] = (ri, hi)
        pan = sorted(pan)
        sh = 0
        mx = 0
        for i in xrange(K-1):
            r, h = pan[i]
            v = 2*pi*h*r
            heappush(q, v)
            sh += v
            mx = pi*r*r + sh
        for i in xrange(K-1, N):
            r, h = pan[i]
            v = 2*pi*h*r
            mx = max(mx, pi*r*r + sh + v)
            if q:
                oldv = heappop(q)
                heappush(q, max(v,oldv))
                if v > oldv:
                    sh += v - oldv

        res = mx
        print 'Case #%d: %0.6f' % (_tc+1, res)
f()

