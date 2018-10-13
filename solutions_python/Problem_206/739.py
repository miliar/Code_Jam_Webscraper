#! /usr/bin/env pypy
#
# author: cy7M4KDaktRcoK8aznGukLJpDtI

import sys
from itertools import chain

MP = 4

def solve(args):
    d, n, ks = args
    th = (1.*(d-k)/s for (k, s) in ks)
    t = max(th)
    v = 1.*d/t
    return v

readin = lambda: sys.stdin.readline().strip()
readinl = lambda: sys.stdin.readline().strip().split()

def getcase():
    d, n = map(int, readinl())
    ks = [map(int, readinl()) for _ in xrange(n)]
    return (d, n, ks)

n = int(readin())
arglist = (getcase() for _ in xrange(n))

if MP:
    import multiprocessing
    mpool = multiprocessing.Pool(MP)
    reslist = mpool.imap(solve, arglist)
else:
    reslist = (solve(_) for _ in arglist)

for i, r in enumerate(reslist):
    print("Case #{}: {}".format(i+1, r))

