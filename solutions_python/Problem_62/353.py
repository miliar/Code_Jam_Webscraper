#!/usr/bin/python

import sys
from fractions import Fraction

sin = sys.stdin

ONE  = Fraction(1,1)
ZERO = Fraction(0,1)

T = int(sin.readline().rstrip('\n'))

for t in xrange(1,T+1):
    N = int(sin.readline().rstrip('\n'))
    A = []
    B = []
    dots = {}
    for n in xrange(0,N):
        line = sin.readline().rstrip('\n').split()
        A.append(int(line[0]))
        B.append(int(line[1]))
    for i in xrange(0,N):
        for j in xrange(0,i):
            hi = B[i]-A[i]
            hj = B[j]-A[j]
            ki = A[i]
            kj = A[j]

            if hi == hj:
                if ki == kj:
                    x = ZERO
                    y = Fraction(ki,1)
                    dots[x,y] = True
            else:
                x = Fraction(ki - kj, hj - hi)
                y = Fraction(hi,1)*x + Fraction(ki,1)
                if ZERO < x < ONE:
                    dots[x,y] = True

    print ('Case #' + str(t) + ': ' + str(len(dots)))
