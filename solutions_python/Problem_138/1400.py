#!/usr/bin/python
import sys
r1 = lambda: sys.stdin.readline()
T = int(r1())
for n in xrange(T):
    N = int(r1())
    naomi = map(float, r1().split())
    ken = map(float, r1().split())
    naomi.sort(reverse=True)
    ken.sort(reverse=True)
    naomi2 = naomi[:]
    ken2 = ken[:]

    c = len(naomi)
    while c >= 0:
        for i in xrange(len(naomi)):
            if naomi[i] < ken[i]:
                ken.remove(ken[i])
                naomi.remove(naomi[-1])
                break
        c = c - 1
    v1 = len(naomi)

    kv = 0
    for i in xrange(len(ken2)):
        c = ken2[i]
        for cc in naomi2:
            if c > cc:
                naomi2.remove(cc)
                kv = kv + 1
                break
    v2 = N - kv
    print "Case #%d: %d %d" % (n+1, v1, v2)
