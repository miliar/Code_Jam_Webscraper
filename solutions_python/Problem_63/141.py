#!/usr/bin/python

def memoize(f):
    cache = {}
    def _f(*args):
        if args in cache:
            return cache[args]
        else:
            v = f(*args)
            cache[args] = v
            return v
    return _f

@memoize
def solve(l, p, c):
    if c * l >= p: return 0
    else:
        lower = l * c
        upper = p / c + 2
        if lower > upper: lower, upper = upper, lower
        try:
            v =min((1 + max(solve(l, k, c), solve(k, p, c)) for k in xrange(lower, upper)))
        except: v = 1
        return v

import sys
f = open(sys.argv[1])
numcases = int(f.next())
for i in xrange(1, numcases + 1):
    l, p, c = map(int, f.next().split(' '))
    print 'Case #%i: %i'%(i, solve(l, p, c))

