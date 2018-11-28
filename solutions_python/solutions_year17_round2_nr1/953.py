#!/usr/bin/env python
import sys
import numpy as np
import decimal
from decimal import Decimal

def get_result(D, N, velocity, inits):
    if N == 1:
        time = (D-inits[0])/velocity[0]
        result = D/time
    else:
        times = (D-inits)/velocity
        result = D/np.max(times)
        #index = np.argsort(inits)
        #inits = inits[index]
        #velocity = velocity[index]
        #times = (D-inits)/velocity
        #if times[0]>times[1]:
        #    result = D/times[0]
        #else:
        #    result = D/times[1]
    return result

if __name__=='__main__':
    infile = sys.argv[1]
    fin = open(infile,mode='r')
    Ncase = int(fin.readline().rstrip())
    for i in xrange(Ncase):
        line = fin.readline().rstrip()
        D = float(line.split()[0])
        N = int(line.split()[1])
        velocity = np.zeros(N)
        inits = np.zeros(N)
        for j in xrange(N):
            line = fin.readline().rstrip()
            inits[j] = float(line.split()[0])
            velocity[j] = float(line.split()[1])

        result = get_result(D, N, velocity, inits)
        print "Case #%d: %.7f" % (i+1, result)



