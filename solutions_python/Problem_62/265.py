#!/usr/bin/python

import os.path
import itertools


def getResult():
    return ""

largeFile = "A-large.in"
smallFile = "A-small-attempt1.in"
inputFile = ""
if  os.path.exists(largeFile):
    inputFile = largeFile
else:
    inputFile = smallFile
outputFile = open(inputFile.split(".")[0] + ".out", 'w')
input = open(inputFile)

caseNum = int(input.readline().strip())

N = 0
for test in range(15):
    wires = []
    N = int(input.readline().strip())
    #print N
    for i in range(N):
        points = input.readline().strip().split()
        wires.append((int(points[0]), int(points[1])))
    sum = 0
    if N > 1:
        for pair in itertools.combinations(wires, 2):
            #print pair

            if (pair[0][0] - pair[1][0]) < 0 and (pair[0][1] - pair[1][1]) > 0:
                sum += 1
            elif (pair[0][0] - pair[1][0]) > 0 and (pair[0][1] - pair[1][1]) < 0:
                sum += 1

    result = 'Case #{0}: {1}'.format(test + 1, str(sum))
    #print result
    outputFile.write(result + "\n")

input.close()
outputFile.close()
