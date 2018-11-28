#!/usr/bin/python

from sys import stdin
from itertools import *


n = int(stdin.readline())

for i in xrange(1, n + 1):
    l = stdin.readline()[:-1]
    t = map(int, l.split())
    n = t[0]
    s = t[1]
    p = t[2]
    t = t[3:]
    a = len(filter(lambda x: x >= max(p * 3 - 2, 0), t))

    b = min(len(filter(lambda x: max(p * 3 - 2, 0) > x >= max(p * 3 - 4, 2), t)), s)

    print "Case #%d: %d" % (i, a+b)

