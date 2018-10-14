#!/usr/bin/env python

import numpy as np

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    N, K = [int(x) for x in raw_input().split()]
    A, B = [0]*N, [0]*N
    for i in xrange(N):
        R, H = [int(x) for x in raw_input().split()]
        RH = R*H
        A[i], B[i] = (RH, R), (R, RH)
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    max_R = 0
    for i in xrange(K):
        max_R = max(max_R, A[i][1])
    max_val = 2*sum([x[0] for x in A[:K-1]])
    max_sum = max_val + 2*A[K-1][0] + max_R**2
    for i in xrange(len(B)):
        if B[i][0] <= max_R:
            break
        else:
            max_sum = max(max_val+2*B[i][1]+B[i][0]**2, max_sum)
    print np.pi * max_sum

