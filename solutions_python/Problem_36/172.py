#!/usr/bin/python

import sys
from scipy import *



def main():
    NN = int(sys.stdin.next())
    for nn in xrange(1,NN+1):
        sys.stdout.write('Case #%d: ' % nn)
        calculate()
        

def calculate():
    R = ' ' + sys.stdin.next().strip()
    C = ' welcome to code jam'

    t = zeros([len(R), len(C)], dtype='int')
    for r in range(1,len(R)):
        t[r][0] = 1
        for c in range(1,len(C)):
            t[r][c] = t[r-1][c] + (R[r]==C[c] and t[r][c-1])
            t[r][c] %= 10000
    print '%04d' % t[-1][-1]


    
if __name__ == "__main__":
    main()
