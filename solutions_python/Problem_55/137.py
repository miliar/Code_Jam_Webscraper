#!/usr/bin/python
import string, sys

nr = string.atoi(sys.stdin.readline().strip())
for i in range(nr):
    R, k, N = map(lambda x: string.atoi(x), sys.stdin.readline().strip().split())
    g = map(lambda x: string.atoi(x), sys.stdin.readline().strip().split())

    res = 0
    giter = 0
    cache = {}
    j = 0

    while j < R:
        if cache != None:
            cache[giter % N] = (j, res)
        ki = k
        gend = giter + N

        while (ki > 0) and (giter < gend) and g[giter % N] <= ki:
            gi = g[giter % N]
            ki -= gi
            res += gi
            giter += 1

        j += 1

        if cache != None and cache.has_key(giter % N):
            jold, resold = cache[giter % N]
            jdiff, resdiff = j - jold, res - resold

            nr = (R - j) // jdiff
            if nr > 0:
                j += nr * jdiff
                res += nr * resdiff
                cache = None

    print 'Case #%d: %d' % (i + 1, res)
