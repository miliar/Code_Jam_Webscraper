#! /usr/bin/env pyp
#
# author: cy7M4KDaktRcoK8aznGukLJpDtI

import sys
from itertools import chain

MP = 0

def solve(args):
    # B-small
    n, r, o, y, g, b, v = args
    # assert n == r + y + b
    # assert o == g == v == 0
    d = {"R":r, "Y":y, "B":b}
    if r == y == b == 0:
        return "IMPOSSIBLE"
    ryb_cnt = list(sorted([r, y, b]))
    if ryb_cnt[0:2] == [0, 0]:
        return "IMPOSSIBLE"
    prevalentcol = None; cnt = 0
    for c, x in d.iteritems():
        if x > cnt:
            prevalentcol = c
            cnt = x
    othercolorcount = sum(d[_] for _ in set(d)-set([prevalentcol]))
    if othercolorcount < d[prevalentcol]:
        return "IMPOSSIBLE"
    def ocgen(d, prevalentcol):
        d = d.copy()
        del d[prevalentcol]
        while 1:
            if set(d.values()) == set([0]):
                raise StopIteration
            col = list(sorted(((_[1], _[0]) for _ in d.iteritems()), reverse=True))[0][1]
            yield col
            d[col] -= 1
    rl = []
    npc = d[prevalentcol]
    ocg = ocgen(d, prevalentcol)
    for i in xrange(npc):
        rl.append(prevalentcol)
        if i == npc - 1:
            for x in ocg:
                rl.append(x)
        else:
            rl.append(ocg.next())
    return "".join(rl)


readin = lambda: sys.stdin.readline().strip()
readinl = lambda: sys.stdin.readline().strip().split()

def getcase():
    return map(int, readinl())

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

