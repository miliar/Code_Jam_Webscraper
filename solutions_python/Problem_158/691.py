#!/usr/bin/env python

import sys


def token_stream():
    for s in sys.stdin:
        for x in s.rstrip().split():
            yield x

def solve(x, r, c):
    if r > c:
        r, c = c, r
    if r * c % x != 0:
        return False
    if x == 1:
        return True
    if x == 2:
        return r + c > 2
    if x == 3:
        return r >= 2 and c >= 3
    if x == 4:
        return c >= 4 and r >= 3
    return False

inp = token_stream()

T = int(next(inp))
for case in xrange(T):
    x = int(next(inp))
    r = int(next(inp))
    c = int(next(inp))

    print "Case #{}: {}".format(case + 1, "GABRIEL" if solve(x, r, c) else "RICHARD")

