from __future__ import division

import os
import sys
from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
#from collections import defaultdict
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'B-small-attempt0'
#name = 'B-micro'

impossible = "IMPOSSIBLE"

def _solve(V, X, RCs):
    lower = []
    higher = []
    sum_r = 0
    for r,c in RCs:
        if c < X:
            lower.append((r,c))
        elif c > X:
            higher.append((r,c))
        else:
            sum_r += r

    lower = list(reversed(sorted(lower)))
    higher = list(sorted(higher))

    while len(lower) > 0 and len(higher) > 0:
        lor, loc = lower.pop(0)
        hir, hic = higher.pop(0)
        if lor*(X-loc) <= hir*(hic-X):
            real_lo = lor 
            real_hi = lor * (X-loc) / (hic-X)
            higher.insert(0, (hir - real_hi, hic))
        else:
            real_hi = hir
            real_lo = hir * (hic-X) / (X-loc)
            lower.insert(0, (lor - real_lo, loc))
        sum_r += real_hi + real_lo

    if sum_r == 0:
        return impossible
    else:
        res = V / sum_r
        if res > 10**12:
            return impossible
        else:
            return res


def format(out):
    return out

def solve(*args, **kwargs):
    return format(_solve(*args, **kwargs))

print(solve(10, 50, ((0.2, 50),)), 50)
print(solve(30.0000, 65.4321, ((0.0001, 50.0000), (100.0000, 99.9000))), 207221.843687375)

#sys.exit(0)

os.system('cp /home/mama/Downloads/%s.in .'%name)
os.system('rm /home/mama/Downloads/%s*.in'%name)
lines = open('%s.in'%name).readlines()
output = open('%s.out'%name, 'w')
cases = int(lines[0])
curline = 1
for caseno in range(cases):
    N,V,X = tuple(x for x in lines[curline].split())
    N = int(N)
    V = float(V)
    X = float(X)
    curline += 1
    inp = []
    for _ in range(N):
        inp.append(tuple(float(x) for x in lines[curline].split()))
        curline += 1
    inp = tuple(inp)
    res = str(solve(V,X,inp))
    #print(inp, caseno, res)
    print('---')
    output.write('Case #%d: %s\n'%((caseno+1), res))
    output.flush()
output.close()
    








