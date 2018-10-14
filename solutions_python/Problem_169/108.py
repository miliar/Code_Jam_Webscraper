import os
import sys
import resource


for cases in range(int(raw_input())):
    x = raw_input().split()
    n = int(x[0])
    v = float(x[1])
    x = float(x[2])
    r = [0]*n
    c = [0]*n
    for i in range(n):
        r[i], c[i] = map(float, raw_input().split())

    if n == 1:
        if c[0] == x:
            print "Case #%d: %.7lf" %(cases+1, v/(r[0]))
        else:
            print "Case #%d: IMPOSSIBLE" %(cases+1,)
    elif abs(c[0] - x) < 0.00001 and abs(c[1] - x) < 0.00001:
        print "Case #%d: %.7lf" %(cases+1, v/(r[0]+r[1]))
    elif abs(c[0] - x) < 0.00001 or abs(c[1] - x) < 0.00001:
        xx = (c[1] == x)
        print "Case #%d: %.7lf" %(cases+1, v/(r[xx]))
    else:
        yy = r[1]*c[1] - r[1] * x
        xx = r[0]*c[0] - r[0] * x
        t1 = v / (r[0] - xx/yy*r[1])
        t2 = - xx / yy * t1
        if t1 < 0 or t2 < 0:
            print "Case #%d: IMPOSSIBLE" %(cases+1,)
        else:
            print "Case #%d: %.7lf" %(cases+1, max(t1, t2))

