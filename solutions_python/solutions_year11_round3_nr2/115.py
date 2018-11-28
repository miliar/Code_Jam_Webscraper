from collections import *
from itertools import *

def solve(l, t, n, c, ds):
    tt = [0]
    for d in islice(cycle(ds), n+1):
        tt.append(tt[-1] + d)

    def boost(cc):
        s = 0
        for i in cc:
            d = tt[i+1] - tt[i]
            if t < tt[i]-s:
                s += d//2
            elif t - (tt[i] - s) < d:
                s += (d - (t - (tt[i]- s)))//2
        return s

    return tt[n] - max(boost(cc) for cc in combinations(range(n), l))

def main(L):
    for t in range(1, 1+int(L[0])):
        xs = map(int, L[t].split())
        print 'Case #%d: %d' % (
            t, solve(xs[0], xs[1], xs[2], xs[3], [x*2 for x in xs[4:]]))

import sys
main(list(sys.stdin))
