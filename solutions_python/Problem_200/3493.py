#! /usr/bin/env pypy
#
# author: cy7M4KDaktRcoK8aznGukLJpDtI

import sys

MP = 1

def solve(args):
    (s,) = args
    s = s.lstrip("0")
    if len(s) == 1: return s
    l = [ int(_) for _ in s ]; ll = len(l)
    pos = None
    for p in xrange(ll-1):
        if l[p] > l[p+1]:
            pos = p
            break
    if pos is None: return s
    for p in xrange(pos+1, ll): l[p] = 0
    return solve([str(max(int("".join(map(str,l)))-1,0))])

n = int(sys.stdin.readline().strip())
arglist = ( sys.stdin.readline().strip().split() for _ in xrange(n) )

if MP:
    import multiprocessing
    mpool = multiprocessing.Pool(4)
    reslist = mpool.imap(solve, arglist)
else:
    reslist = (solve(_) for _ in arglist)

for i, r in enumerate(reslist):
    print("Case #{}: {}".format(i+1, r))

