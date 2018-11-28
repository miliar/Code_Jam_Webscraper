from itertools import izip_longest
from collections import defaultdict

def combine(c1, c2):
    if c1 is None:
        return c2
    if c2 is None:
        return c1
    max_val = max((el[1] for el in c1), (el[1] for el in c2))
    d = defaultdict(list)
    for ix1, vx1 in c1:
        for ix2, vx2 in c2:
            d[ix1+ix2].append(max(vx1, vx2))
    return [(m, min(d[m])) for m in sorted(d.iterkeys()) if m <= max_val]


T = input()

for casenbr in range(T):
    D = input()
    Pis = [int(n) for n in raw_input().split()]
    Pis.sort(reverse=True)
    combs = [[(m-1, A/m + (1 if A%m else 0)) for m in range(1, A+1)] for A in Pis]
    while len(combs) > 1:
        combs = [combine(c1, c2) for c1, c2 in izip_longest(combs[0::2], combs[1::2])]

    print "Case #%d: %d" % (casenbr+1, min(ix+vx for ix, vx in combs[0]))
