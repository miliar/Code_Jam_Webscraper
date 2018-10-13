# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
N = int(fin.readline())
for case in range(1,N+1):
    n = int(fin.readline())
    seq = map(int, fin.readline().split())
    wrong = 0
    for i, k in enumerate(seq):
        if i+1 != k:
            wrong += 1
    
    print "Case #%d: %.6f" % (case, wrong)
