# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
T = int(fin.readline())
for case in range(1,T+1):
    C, D = map(int, fin.readline().split())
    endP = -100000
    most = 0
    total = 0
    for i in range(C):
        P, V = map(int, fin.readline().split())
        if endP + D < P:
            # Start over
            endP = P-D
        
        endP += D*V
        most = max(most, endP-P)
        
    result = most / 2.0
    
    print "Case #%d: %.2f" % (case, result)
