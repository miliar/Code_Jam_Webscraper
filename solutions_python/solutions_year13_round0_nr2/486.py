
# py2

import sys

inp = list(reversed(map(int, sys.stdin.read().split())))

T = inp.pop()

for caseno in xrange(T):
    H = inp.pop()
    W = inp.pop()
    f = [[None] * W for y in xrange(H)]
    mr = [0] * H
    mc = [0] * W
    for y in xrange(H):
        for x in xrange(W):
            f[y][x] = inp.pop()
            mr[y] = max(mr[y], f[y][x])
            mc[x] = max(mc[x], f[y][x])
    bad = False
    for y in xrange(H):
        for x in xrange(W):
            if f[y][x] != min(mr[y], mc[x]):
                bad = True
    print "Case #{}: {}".format(caseno+1, "YES" if not bad else "NO")
