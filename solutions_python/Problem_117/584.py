#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sys import stderr
from collections import deque, defaultdict
from itertools import *
data = deque(map(int,sys.stdin.read().split()))
token = data.popleft
T = int(token())

def test():
    h = defaultdict(lambda:100)
    v = defaultdict(lambda:100)

    H = token()
    W = token()

    l = [ [token() for _ in range(W)] for _ in range(H)]
    lT = zip(*l)

    for i, r in enumerate(l):
        h[i] = max(r)

    for i, r in enumerate(lT):
        v[i] = max(r)

    for hi, r in enumerate(l):
        for vi, el in enumerate(r):
            if not el in (h[hi], v[vi]):
                return "NO"

    return "YES"


for case in xrange(1, T+1):
    print "Case #%d: %s" % (case, test())
    sys.stdout.flush()
