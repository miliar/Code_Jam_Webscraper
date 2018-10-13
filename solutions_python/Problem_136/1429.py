#!/usr/bin/python
import sys
r1 = lambda: sys.stdin.readline()
T = int(r1())
for n in xrange(T):
    c, f, x = map(float, r1().split())
    t = set([x/2])
    xt = x/2
    ct = c/2
    st = 0
    i = 0
    cc = 2
    for j in xrange(int(x/c)):
        ct = c / cc
        st = st + ct
        i = i+1
        cc = (i * f) + 2
        xt = x / cc
        t.add(st + xt)
    print "Case #%d: %.7f" % (n+1, min(t))
