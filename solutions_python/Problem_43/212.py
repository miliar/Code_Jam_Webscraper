#!/usr/bin/env python

import sys

def solve(a):
    res = ''
    s = set(a)
    d = dict.fromkeys(s, '')

    if (len(a)) == 1:
        return 1

    d[a[0]] = '1'
    num = 0
    for c in a:
        if d[c] == '':
            d[c] = str(num)
            if num == 0:
                num = 2
            else:
                num += 1
        res += d[c]

    if len(s) > 1:
        base = len(s)
    else:
        base = 2
    return int(res, base)

T = int(sys.stdin.readline())

for n in xrange(1, T + 1):
    a = sys.stdin.readline().strip()
    print "Case #%s: %s" % (n, solve(a))
