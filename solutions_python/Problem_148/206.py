#!/usr/bin/env python
#-*- coding: utf-8 -*-

from collections import defaultdict
from math import factorial as f
from fractions import gcd as g

T = int (raw_input ())
for t in range (1, T + 1):
    n, c = [int (i) for i in raw_input ().split ()]
    l = [int (i) for i in raw_input ().split ()]
    l.sort ()
    lo, hi = 0, n - 1
    ret = 0
    while lo <= hi:
        if l [lo] + l [hi] <= c:
            ret += 1
            lo += 1
            hi -= 1
        else:
            ret += 1
            hi -= 1
    print ("Case #{0}: {1}".format (t, ret))
