# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
T = int(fin.readline())
for case in range(1,T+1):
    (N,k) = map(int, fin.readline().split())
    m = pow(2,N)
    #print m
    if (k+1) % m == 0:
        print "Case #%d: ON" % (case)
    else:
        print "Case #%d: OFF" % (case)
