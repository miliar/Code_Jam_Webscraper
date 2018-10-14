#!/usr/bin/env python

import itertools
import os.path as path
from collections import namedtuple, Counter
import pprint
import math
import numpy as np # http://www.numpy.org/

def rem(t, count, r):
    return   t - 2*(count**2) - (2*r -1 )*count

def solve(t, r):
    s = 2*r+1
    ans = (s-2 - math.sqrt((s-2)**2 + 8*t))/(-4)
    if rem(t, int(ans), r) < 0:
        return int(ans) - 1
    else:
        return int(ans)

if __name__ == '__main__':
    ans = []
    T = int(raw_input())

    for i in xrange(T):
        r, t = map(int, raw_input().strip().split())
        print 'Case #%d:'%(i+1), solve(t, r)