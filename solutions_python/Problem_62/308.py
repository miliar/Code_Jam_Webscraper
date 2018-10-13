#!/usr/bin/python

import sys

filename = sys.argv[1]

#filename = 'test.txt'

inputFile = open(filename, 'r')
outputFile = open('output.txt', 'w')

T = int(inputFile.readline())

for i in range(T):
    N = int(inputFile.readline())
    A2B = {}
    B2A = {}
    inters = 0
    for k in range(N):
        AandB = inputFile.readline().split()
        A = int(AandB[0])
        B = int(AandB[1])
        #print N, K
        A2B[A] = B
        B2A[B] = A
    Bs = A2B.values()
    As = B2A.values()
    Bs.sort()
    As.sort()
    for j in range(len(As)):
        pivot = Bs[0]
        dist = As.index(B2A[pivot])
        Bs.remove(pivot)
        As.pop(dist)
        A2B.pop(B2A[pivot])
        del B2A[pivot]
        inters = inters + dist
    outputFile.write('Case #' + str(i+1) + ': ' + str(inters) + '\n')
        



inputFile.close()
outputFile.close()

