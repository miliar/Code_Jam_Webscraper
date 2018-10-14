import sys
from collections import defaultdict
from math import floor, ceil

def lohi(v, r):
    lo = v/1.1
    hi = v/.9
    lor = int(ceil(lo / r)) + 1
    hir = int(floor(hi / r)) - 1
    while r*lor*1.1 >= v:
        lor -= 1
    lor += 1
    while r*hir*.9 <= v:
        hir += 1
    hir -= 1
    if hir < lor:
        return None
    return lor, hir

def run(N, P, R, g):
    pointers = [0]*N

    def check():
        vals = [g[i][p] for i,p in enumerate(pointers)]
        lohis = [lohi(v,r) for v,r in zip(vals, R)]
        for i,x in enumerate(lohis):
            if x is None:
                return False, i
        lowesthi = min([hi for lo,hi in lohis])
        highestlow = max([lo for lo,hi in lohis])
        if lowesthi >= highestlow:
            return True, -1
        # find the guy with the lowesthi and raise it
        for i, lohi_ in enumerate(lohis):
            if lohi_[1] == lowesthi:
                return False, i

    ans = 0

    while True:
        good, i = check()
        if good:
            ans += 1
            for x in range(N):
                if pointers[x] == P-1:
                    return ans
                pointers[x] += 1
        else:
            if pointers[i] == P-1:
                return ans
            pointers[i] += 1

f = file(sys.argv[1],'r')
T = int(f.readline().strip())
for case in range(1,T+1):
    N,P = [int(X) for X in f.readline().strip().split()]
    R = [int(X) for X in f.readline().strip().split()]
    g = [sorted([int(X) for X in f.readline().strip().split()]) for i in range(N)]
    ans = run(N, P, R, g)
    print 'Case #%d: %s' % (case, ans)
