# Code Jam 2017 round 1A
# MichelJ
# Problem B: Ratatouille 

from math import ceil, floor
from itertools import product, permutations

def count(ser, np):
    maxkit = 0
    for p in product(*[permutations(r, np) for r in ser]):
        ok = True
        nkit = 0
        # print p
        for i in xrange(np):
            mins, maxs = 0, 9999999
            for c in p:
                mi, ma = c[i]
                if mi > mins:
                    mins = mi
                if ma < maxs:
                    maxs = ma
                if mins > maxs:
                    ok = False
                    break
            if ok:
                nkit += 1
        if nkit > maxkit:
            maxkit = nkit
            if maxkit == np:
                return np
    return maxkit
        

def solve(n, p, r, q):
    minser = [[0 for j in xrange(p)] for i in xrange(n)]
    maxser = [[0 for j in xrange(p)] for i in xrange(n)]
    ser = [[] for i in xrange(n)]
    for i in xrange(n):
        rimax = r[i] * 1.1
        rimin = r[i] * 0.9
        for j in xrange(p):
            mins = int(ceil(q[i][j] / rimax))
            maxs = int(floor(q[i][j] / rimin))
            if mins <= maxs:
                minser[i][j] = mins
                maxser[i][j] = maxs
                ser[i].append((mins, maxs))
        ser[i].sort()
    np = min(len(r) for r in ser)
    if np == 0:
        return 0
    return count(ser, np)

def main():
    for t in xrange(input()):
        n, p = map(int, raw_input().split())
        r = map(int, raw_input().split())
        q = [map(int, raw_input().split()) for _ in xrange(n)]
        res = solve(n, p, r, q)
        print "Case #%d: %d"%(t + 1, res)
        
#main()

from multiprocessing import Pool

def f(arg):
    return solve(*arg)

def main_mp():
    args = []
    for t in xrange(input()):
        n, p = map(int, raw_input().split())
        r = map(int, raw_input().split())
        q = [map(int, raw_input().split()) for _ in xrange(n)]
        # res = solve(n, p, r, q)
        args.append((n, p, r, q))
    p = Pool(8)
    sols = p.map(f, args)
    for t, res in enumerate(sols):
        print "Case #%d:"%(t + 1), res

if __name__ == '__main__':
    main_mp()
