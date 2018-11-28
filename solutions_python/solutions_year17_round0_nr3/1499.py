#!/usr/bin/python

# To force float division for integers
from __future__ import division

import sys

from math import floor
from math import ceil

inputFile = 'C-small-2-attempt0.in'
f = open(inputFile, 'r')

def main(argv):
    T = int(f.readline())
    for i in range(1, T+1):
        line = f.readline()[:-1]
        N, K = [int(j) for j in line.split(' ')]
        numberOfCells = getMaxFreeCells(N, K)
        maxEmptyCells = int(ceil((numberOfCells-1)/2))
        minEmptyCells = int(floor((numberOfCells-1)/2))
        #print N, K
        print("Case #%r: %r %r" % (i, maxEmptyCells, minEmptyCells))

# No need to compute the exact location of the cells
# This method returns the amount of empty stalls to select the Kth stall from
def getMaxFreeCells(N, K):
    while K != 1:
        #print("K = %r and N = %r" % (K, N))
        left = int(floor((N-1)/2))
        right = int(ceil((N-1)/2))
        zeroMeansRight = right > left
        zeroMeansLeft = not zeroMeansRight
        # Modulo in python is always positive
        direction = K%2
        if direction == 0:
            if zeroMeansLeft:
                N = left
            else:
                N = right
        elif direction == 1:
            if zeroMeansLeft:
                N = right
            else:
                N = left
        K = int(K/2)
    return N

if __name__ == '__main__':
    main(sys.argv[1:])

