#!/usr/bin/env python2
from __future__ import division, print_function

import sys
import math
from itertools import izip, tee
from pprint import pprint as pp
from collections import Counter, namedtuple
import operator as op


def dbg(*args, **kwargs):
    #return
    kwargs['file'] = sys.stderr
    print('.', *args, **kwargs)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def result(m):
    diffs = tuple(b-a for (a,b) in pairwise(m))
    y = - sum(d for d in diffs if d<=0)
    z = 0
    rate = - min(d for d in diffs if d<=0)  # pieces / 10s
    for a, b in pairwise(m):
        z += (min(rate, a))

    return (y, z)


if __name__ == '__main__':
    #sys.setrecursionlimit(max(2000, sys.getrecursionlimit()))
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        print('===', t+1, '===', file=sys.stderr)

        N = int(sys.stdin.readline().strip())
        m = tuple(int(tk) for tk in sys.stdin.readline().strip().split())
        assert(len(m) == N)

        #if t+1 != 8: continue

        y, z = result(m)
        print('Case #{}: {} {}'.format(t+1, y, z))
        sys.stdout.flush()

