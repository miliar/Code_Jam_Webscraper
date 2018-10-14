#!/usr/bin/env python

import sys

def gcd(x, y):
    return gcd(y, x % y) if y else x

T = int(sys.stdin.readline())
for x in xrange(1, T + 1):
    N, P_D, P_G = tuple(int(e) for e in sys.stdin.readline().split())
    m = 100 / gcd(100, P_D)
    if m <= N and not ((P_G == 100 and P_D != 100) or (P_G == 0 and P_D != 0)):
        y = 'Possible'
    else:
        y = 'Broken'
    sys.stdout.write('Case #%d: %s\n' % (x, y))
