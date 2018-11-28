#! /usr/bin/env python

import sys

def cookie_time(C, F, X):
    dCdT = 2.0
    t = 0.0
    while X/dCdT > C/dCdT + X/(dCdT+F):
        t += C/dCdT
        dCdT += F
    t += X/dCdT
    return t

if __name__ == '__main__':
    with open(sys.argv[1]) as testdata:
        t = int(testdata.readline())
        for i in range(1, t+1):
            C, F, X = [float(x) for x in testdata.readline().split()]
            print "Case #{}: {:.7f}".format(i, cookie_time(C, F, X))
