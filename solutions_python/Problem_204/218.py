#!/usr/bin/env python
#coding:utf-8
#py 2
import sys
sys.setrecursionlimit(10000000)
from itertools import permutations
import math
def get_lr(q, r):
    n1 = math.floor(q/(r*0.9))
    n2 = math.ceil(q/(r*1.1))
    #[1, n1] [n2, inf]
    #n1 >= n2
    return int(n2), int(n1)
T = int(raw_input().strip())
for cas in xrange(1, T+1):
    #N 1 2 P 1 8 P^N is not large
    N, P = map(int, raw_input().strip().split())
    R = map(int, raw_input().strip().split())
    Q = [map(int, raw_input().strip().split()) for i in xrange(N)]
    res = 0
    if N == 1:
        for i in xrange(P):
            #ceil and floor?
            l, r = get_lr(Q[0][i], R[0])
            if l > 0 and r >= l:
                res += 1
    elif N == 2:
        a = Q[0][:]
        b = Q[1][:]
        for p in permutations(b):
            cnt = 0
            for i in xrange(P):
                la, ra = get_lr(a[i], R[0])
                lp, rp = get_lr(p[i], R[1])
                if la > 0 and ra >= la and lp > 0 and rp >= lp:
                    l = max(la, lp)
                    r = min(ra, rp)
                    if l <= r:
                        cnt += 1
            res = max(res, cnt)
    else:
        print 'Error', N
        break
    print "Case #%s: %d"%(cas, res)
