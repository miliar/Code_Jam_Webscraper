#!/usr/bin/python

from sys import stdin
from itertools import *


n = int(stdin.readline())

for k in xrange(1, n + 1):
    l = stdin.readline()[:-1]
    t = map(int, l.split())
    a = t[0]
    b = t[1]

    res = 0
    for i in xrange(a, b + 1):
        s = str(i)

        was = set()

        for c in xrange(1, len(s)):
            z = int(s[c:] + s[:c])
            if (len(str(z)) != len(s)):
                continue
            if z in was:
                continue
            if a <= i < z <= b:
                was.add(z)
                res += 1

    print "Case #%d: %d" % (k, res)

