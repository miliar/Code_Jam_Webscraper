from __future__ import division
import sys, heapq

def fw(g):
    N = len(g)
    for k in xrange(N):
        for i in xrange(N):
            for j in xrange(N):
                a = g[i][k]
                b = g[k][j]
                if a is None or b is None:
                    continue
                c = g[i][j]
                if c is None or c > a + b:
                    g[i][j] = a + b

toks = open(sys.argv[1], 'r').read().split()
toks.reverse()

T = int(toks.pop())
for t in xrange(T):
    N = int(toks.pop())
    Q = int(toks.pop())

    horses = []
    for _ in xrange(N):
        E = int(toks.pop())
        S = int(toks.pop())
        horses.append((E, S))

    D = [[None]*N for _ in xrange(N)]
    for i in xrange(N):
        for j in xrange(N):
            x = int(toks.pop())
            if x != -1:
                D[i][j] = x
        D[i][i] = 0

    fw(D)

    g = [[None]*N for _ in xrange(N)]
    for i, (E, S) in enumerate(horses):
        for j in xrange(N):
            d = D[i][j]
            if d is not None and d <= E:
                g[i][j] = d / S

    fw(g)

    r = []
    for _ in xrange(Q):
        U = int(toks.pop())
        V = int(toks.pop())
        r.append(str(g[U-1][V-1]))

    print 'Case #{}: {}'.format(t+1, ' '.join(r))
