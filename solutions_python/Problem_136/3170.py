#!/usr/bin/python
import sys

N = int(sys.stdin.readline())

for case in xrange(N):
    C, F, X = map(float,sys.stdin.readline().split())
    n_farms_f = (F*X - 2*C)/(C*F) - 1.
    n_farms = int((F*X - 2*C)/(C*F) - 1.)
    if n_farms_f > 0:
        t1 = 0.
        for i in xrange(n_farms+1):
            t1 += 1./(2.+i*F) # 2 comes from initial rate
            
        t = C * t1 + (X / (2. + ((n_farms+1) * F)))
    else:
        t = X / 2.
    print "Case #%d: %.7f" % (case+1, t)

    
    
