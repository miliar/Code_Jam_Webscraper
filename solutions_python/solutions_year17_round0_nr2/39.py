#!/usr/bin/env python
from sys import stdin

def solve2(n, d, l):
    if l == 0:
        return 0
    for i in xrange(9, d-1, -1):
        if int(str(i)*l) <= n:
            s = i * (10**(l-1))
            return s + solve2(n - s, i, l-1)
    assert(False)

def solve(n):
    r = 0
    for l in xrange(1, 50):
        for d in xrange(1, 10):
            x = int(str(d)*l)
            if x == n:
                return n
            if x > n:
                break
        else:
            continue
        break
    d -= 1
    if d == 0:
        d = 9
        l -= 1
    return solve2(min(n, int(str(d)+ '9'*(l-1))), d, l)


tn = int(stdin.readline())
for ti in xrange(tn):
    n = int(stdin.readline())
    print 'Case #{0}:'.format(ti+1), solve(n)
