#!/usr/bin/python

import sys

filename = sys.argv[1]

inputFile = open(filename, 'r')
outputFile = open('output.txt', 'w')

T = int(inputFile.readline())

for i in range(T):
    NandK = inputFile.readline().split()
    N = int(NandK[0])
    K = int(NandK[1])
    #print N, K
    
    state = 'ON'
    for j in range(N):
        qr = divmod(K,2)
        if (qr[1] == 0):
            state = 'OFF'
            break
        K = qr[0]
    outputFile.write('Case #' + str(i+1) + ': ' + state + '\n')
        

inputFile.close()
outputFile.close()
