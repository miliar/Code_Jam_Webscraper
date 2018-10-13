#!/usr/bin/env python
from sys import stdin

tn = int(stdin.readline())
for ti in xrange(tn):
    n, q = map(int, stdin.readline().split())
    e = [0]*n
    s = [0]*n
    for i in xrange(n):
        e[i], s[i] = map(int, stdin.readline().split())
    a = []
    g = [[-1]*n for i in xrange(n)]
    for i in xrange(n):
        a.append(map(int, stdin.readline().split()))
        a[i][i] = 0
        g[i][i] = 0
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if a[i][k] >= 0 and a[k][j] >= 0 and (a[i][j] < 0 or a[i][k] + a[k][j] < a[i][j]):
                    a[i][j] = a[i][k] + a[k][j]
    for i in xrange(n):
        for j in xrange(n):
            if a[i][j] >= 0 and a[i][j] <= e[i]:
                g[i][j] = float(a[i][j])/s[i]
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if g[i][k] >= 0 and g[k][j] >= 0 and (g[i][j] < 0 or g[i][k] + g[k][j] < g[i][j]):
                    g[i][j] = g[i][k] + g[k][j]
    r = []
    for qi in xrange(q):
        u, v = map(int, stdin.readline().split())
        r.append(g[u-1][v-1])

    print 'Case #{}:'.format(ti+1), ' '.join(['{:.6f}'.format(x) for x in r])

