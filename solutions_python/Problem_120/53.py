#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sys import stderr
from collections import deque
from itertools import *
data = deque(map(int,sys.stdin.read().split()))
token = data.popleft
T = int(token())

# Bisect_right
def bisect(b, e, callback):
    if b == e:
        return e - 1

    m = int((b+e)/2)
    if callback(m):
        return bisect(m+1, e, callback)
    else:
        return bisect(b, m, callback)

def test():
    r = token()
    t = token()

    def test(k):
        return 2*k*r + k*(2*k-1) <= t
    return bisect(1, t, test)

for case in xrange(1, T+1):
    print "Case #%d: %s" % (case, test())
    sys.stdout.flush()
