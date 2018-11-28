#!/usr/bin/env python

import sys


def token_stream():
    for s in sys.stdin:
        for x in s.rstrip().split():
            yield x

def solve(s):
    deficit = 0
    clappers = 0
    for i, c in enumerate(s):
        if clappers < i:
            deficit += i - clappers
            clappers = i
        clappers += int(c)
    return deficit


inp = token_stream()

T = int(next(inp))
for case in xrange(T):
    n = next(inp)
    s = next(inp)

    print "Case #{}: {}".format(case + 1, solve(s))

