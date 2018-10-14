#!/usr/bin/python

import numpy as np


def poss(cakes, k):
    counter = 0
    for i in range(len(cakes)):
        c = cakes[i]
        if c == '-':
            counter = counter + 1
            for j in range(k):
                if i + k <= len(cakes):
                    if cakes[i+j] == '-':
                        cakes[i+j] = '+'
                    else:
                        cakes[i+j] = '-'
    print(''.join(cakes) + ' ' + str(k))
    if ''.join(cakes) == '+'*len(cakes):
        return counter
    else:
        return -1



inFile=open('pancakeInput.txt', 'r')
outFile=open('pancakeOutput.txt', 'w')

nrLines = int(inFile.readline())

for i, line in enumerate(inFile):
    arr = line.split()
    cakes = list(arr[0])
    k = int(arr[1])
    flips = poss(cakes, k)
    if flips == -1:
        outFile.write("Case #"+str(i+1)+": IMPOSSIBLE \n")
    else:
        outFile.write("Case #"+str(i+1)+": " + str(flips) + " \n")
inFile.close()
outFile.close()






