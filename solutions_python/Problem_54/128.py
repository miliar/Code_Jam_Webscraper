#!/usr/bin/env python

import sys

def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a

nc = int(sys.stdin.readline().strip())
for c in xrange(nc):
    line = sys.stdin.readline().strip()
    parts = line.split()
    n = int(parts[0])
    t = map(lambda x: int(x), parts[1:])
    ct = abs(t[1] - t[0])
    for i in xrange(n - 2):
        ct = gcd(ct, abs(t[i + 2] - t[0]))
    if t[0] % ct == 0:
        ans = 0
    else:
        ans = ct - (t[0] % ct)
    print "Case #%d: %d" % (c + 1, ans)
