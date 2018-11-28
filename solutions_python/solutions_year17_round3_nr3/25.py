# Do small first

inputF = open('C-small-1-attempt0.in', 'r')
output = open('C-small-1-attempt0.out', 'w')

import math
import operator

numCases = int(inputF.readline())

def getBestProb(coreProbs, unitsToAdd):
    # Just distribute the unitsToAdd evenly
    coreProbs.sort()
    numAccumulating = 1
    while len(coreProbs) > 1 and unitsToAdd >= ((coreProbs[1]-coreProbs[0])*numAccumulating):
        unitsToAdd -= (coreProbs[1]-coreProbs[0])*numAccumulating
        numAccumulating += 1
        coreProbs = coreProbs[1:]
        #print coreProbs, numAccumulating, unitsToAdd
    coreProbs[0] = coreProbs[0] + unitsToAdd/numAccumulating
    #print coreProbs, 
    return math.pow(coreProbs[0], numAccumulating) * reduce(operator.mul, coreProbs[1:], 1)
    

for i in range(numCases):
    n, k = inputF.readline().split()
    u = float(inputF.readline())
    cores = inputF.readline().split()
    cores = [float(x) for x in cores]
    prob = getBestProb(cores, u)
    print i
    #print prob
    output.write('Case #' + str(i+1) + ': ' + str(prob) + '\n')
inputF.close()
output.close()
