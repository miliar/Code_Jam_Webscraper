#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import collections

fin = sys.stdin
T = int(fin.readline())


for case in range(1, T + 1):
    A,B,K = list(map(int,fin.readline().split()))
    count = 0
    
    for x in range(A):
        for y in range(B):
            if (x & y) < K:
                count = count + 1
                

    
    print("Case #%d: %d" % (case, count))
    