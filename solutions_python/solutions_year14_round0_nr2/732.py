#!python
#-*- coding:utf-8 -*-

import sys

T = int( sys.stdin.readline() )
for index in range(T):
    C, F, X = [ float(x) for x in sys.stdin.readline().split() ]
    
    cps  = 2.0
    time = 0.0
    while True:
        t0  = C / cps
        ta0 = X / cps - t0
        ta1 = X / (cps + F)
        if ta0 < ta1:
            time += t0 + ta0
            break
        else:
            time += t0
            cps  += F
    print "Case #%d: %.7f" % ( index + 1, time )
    