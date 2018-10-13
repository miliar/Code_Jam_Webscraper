#!/usr/bin/env python

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
    res = []
    for i in xrange(N):
        res.append(foo())
    return res
def readlinearray(foo): return map(foo, raw_input().split())

def check(freqs, guess):
    for f in freqs:
        if (f % guess != 0) and (guess % f != 0):
            return False
    return True

nTests = readint()
for test in xrange(nTests):
    N, L, H = readlinearray(int)
    freqs = readlinearray(int)
    freqs.sort()

    mi = 10**10
    while L <= H:
        if check(freqs, L):
            mi = L
            break
        L = L + 1

    if mi < 10**10:
        print "Case #%d: %d" % (test + 1, mi)
    else:
        print "Case #%d: NO" % (test + 1)

