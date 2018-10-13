#! /usr/bin/env python

import sys

for i in xrange(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip().split(" ")
    c, d, r = {}, {}, ""
    for j in xrange(int(a.pop(0))):
        x, y, z = list(a.pop(0))
        c[x + y] = c[y + x] = z
    for j in xrange(int(a.pop(0))):
        x, y = list(a.pop(0))
        d[x + y] = d[y + x] = 1
    for x in a[1]:
        r += x
        if r[-2:] in c:
            r = r[:-2] + c[r[-2:]]
        if reduce(lambda a, b: a or (b + r[-1] in d), r[:-1], 0):
            r = ""
    print "Case #%d: [%s]" % (i + 1, ", ".join(r))

# [EOF]
