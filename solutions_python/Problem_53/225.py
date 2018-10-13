# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
N = int(fin.readline())
for case in range(1,N+1):
    n, k = map(int, fin.readline().split())
    
    if k & ((1 << n) - 1) == ((1 << n) - 1):
        result = "ON"
    else:
        result = "OFF"
    print "Case #%d: %s" % (case, result)
