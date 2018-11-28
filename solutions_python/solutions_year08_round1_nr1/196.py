from __future__ import with_statement

import sys

with open(sys.argv[1]) as f:
    t = int(f.readline())
    for l in range(1,t+1):
        n = long(f.readline())
        x = map(long, f.readline().split(' '))
        y = map(long, f.readline().split(' '))
#        print "n: %s, x: %s, y: %s" % (n, x, y)
        x.sort()
        y.sort(reverse=True)
        res = 0
        for i in range(n):
            res += x[i] * y[i]
        print "Case #%s: %s" % (l, res)
