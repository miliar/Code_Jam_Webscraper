#! /usr/bin/python

from sys import stdin

def parsetime(s):
    return int(s[0:2]) * 60 + int(s[3:5])

ncase = int(stdin.readline())

for icase in xrange(1, ncase + 1):
    turn = int(stdin.readline())
    na, nb = [ int(x) for x in stdin.readline().split() ]

    a0 = [ 0 for _ in xrange(1440) ]
    a1 = [ 0 for _ in xrange(1440) ]
    b0 = [ 0 for _ in xrange(1440) ]
    b1 = [ 0 for _ in xrange(1440) ]

    for _ in xrange(na):
        t0, t1 = [ parsetime(x) for x in stdin.readline().split() ]
        a0[t0] += 1
        if 0 < t1 + turn <= 1440: b1[t1 + turn - 1] += 1

    for _ in xrange(nb):
        t0, t1 = [ parsetime(x) for x in stdin.readline().split() ]
        b0[t0] += 1
        if 0 < t1 + turn <= 1440: a1[t1 + turn - 1] += 1

    ma = mb = 0
    wa = wb = 0

    for t in xrange(1440):
        ma += max(a0[t] - wa, 0)
        mb += max(b0[t] - wb, 0)
        wa = max(wa - a0[t], 0) + a1[t]
        wb = max(wb - b0[t], 0) + b1[t]

    print ( "Case #%d: %d %d" % ( icase, ma, mb ) )
