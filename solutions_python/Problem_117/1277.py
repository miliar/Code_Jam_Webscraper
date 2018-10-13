#!/usr/bin/python

import sys
import numpy as np

i = (int(n) for n in sys.stdin.read().split())

T = next(i)

for case in xrange(1,T+1):
    N, M = next(i), next(i)
    NM = np.array([[next(i) for m in xrange(M)] for n in xrange(N)])
    result = 'YES'
    while NM.shape[0] > 1 and NM.shape[1] > 1:
        n, m = NM.shape
        nmin, mmin = np.unravel_index(np.argmin(NM), NM.shape)
        mm = NM[nmin, mmin]
        if max(NM[nmin,...]) == mm:
            NM = np.delete(NM, (nmin,), axis=0)
        elif max(NM[...,mmin]) == mm:
            NM = np.delete(NM, (mmin,), axis=1)
        else:
            result = 'NO'
            break
    print "Case #%d: %s" % (case, result)
