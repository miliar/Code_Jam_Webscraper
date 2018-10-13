#!/usr/bin/env python
from sys import stdin

tn = int(stdin.readline())
for ti in xrange(tn):
    n, r, o, y, g, b, v = map(int, stdin.readline().split())
    s = ''
    if r > 0:
        s = 'R'
        r -= 1
    elif y > 0:
        s = 'Y'
        y -= 1
    else:
        s = 'B'
        b -= 1
    for i in xrange(n-1):
        if s[-1] == 'R':
            if y == 0 and b == 0:
                s = 'IMPOSSIBLE'
                break
            if y > b or (y == b and s[0] == 'Y'):
                s += 'Y'
                y -= 1
            else:
                s += 'B'
                b -= 1
        elif s[-1] == 'Y':
            if r == 0 and b == 0:
                s = 'IMPOSSIBLE'
                break
            if r > b or (r == b and s[0] == 'R'):
                s += 'R'
                r -= 1
            else:
                s += 'B'
                b -= 1
        elif s[-1] == 'B':
            if y == 0 and r == 0:
                s = 'IMPOSSIBLE'
                break
            if y > r or (y == r and s[0] == 'Y'):
                s += 'Y'
                y -= 1
            else:
                s += 'R'
                r -= 1
    if s[0] == s[-1]:
        s = 'IMPOSSIBLE'
    print 'Case #{0}:'.format(ti+1), s
