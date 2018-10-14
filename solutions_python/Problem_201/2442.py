#! /usr/bin/env pypy
#
# author: cy7M4KDaktRcoK8aznGukLJpDtI

import sys

MP = 1

def solve(args):
    n, k = map(int, args)
    spaces = [n]
    mn = mx = n
    for i in xrange(k):
        biggest = max(spaces)
        chosen = spaces.index(biggest)
        if spaces[chosen] < 1: raise ValueError("non-empty!")
        mn = (biggest - 1) // 2
        mx = biggest - mn - 1
        spaces[chosen:chosen+1] = [mn, mx]
    return "{} {}".format(mx, mn)

n = int(sys.stdin.readline().strip())
arglist = (sys.stdin.readline().strip().split() for _ in xrange(n))

if MP:
    import multiprocessing
    mpool = multiprocessing.Pool(4)
    reslist = mpool.imap(solve, arglist)
else:
    reslist = (solve(_) for _ in arglist)

for i, r in enumerate(reslist):
    print("Case #{}: {}".format(i+1, r))

