#!/usr/bin/python


import sys
import numpy as np
import pandas as pd

paint = lambda N,R: N*(N+2*R-1)

def check(N,R,T):
    paintN = paint(N,R)
    n = N
    while paintN > T:
        n -= 1
        paintN = paint(n,R)
    return n

def process_case(R, T):
    t = float(T)
    r = float(R)

    B = (2*r - 1)
    A = float(2)
    C = -t
    x = (-B + np.sqrt(B**2 - 4*A*C))/ (2*A)
    coeffs = np.roots([A,B,C])
    return int(np.floor(x))



############################
# Begin parse of inputfile #
############################

if __name__ == '__main__':

    infile = open(sys.argv[1], 'rb')
    lines = map(lambda x: x.rstrip(), infile.readlines())

    N = int(lines[0])  # Number of cases
    lineIdx = 1
    caseNo = 1

    while (lineIdx < len(lines) and caseNo <= N):
        R, T = map(int, lines[lineIdx].split(' '))
        caseAnswer = check( process_case(R,T), R, T )
        print 'Case #%d: %d' % (caseNo, caseAnswer)
        lineIdx += 1
        caseNo += 1
    


