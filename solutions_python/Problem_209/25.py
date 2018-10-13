inputF = open('A-large.in', 'r')
output = open('A-large.out', 'w')

import math

numCases = int(inputF.readline())

def getMaxSurfaceArea(pancakes, k):
    ''' Pancakes is a list of (radius, height) tuples '''
    pancakes = [(pancakes[i][0], pancakes[i][1]*pancakes[i][0]*2*math.pi) for i in range(len(pancakes))]
    sortedByTallArea = sorted(pancakes, key = lambda x: x[1], reverse=True)
    # Sort by area
    # For each base pancake, check best
    pancakes.sort(reverse=True)
    #print pancakes
    bestSoFar = 0
    for i in range(0, (len(pancakes)-k)+1):
        topArea = math.pi*(pancakes[i][0]**2) + pancakes[i][1]
        filtered = filter(lambda j: pancakes[j][0] <= pancakes[i][0] and j != i, range(len(pancakes)))
        filtered = [pancakes[j] for j in filtered]
        bestFiltered = sorted(filtered, key = lambda x: x[1], reverse=True)[:k-1]
        #print bestFiltered
        bestFiltered = sum([x[1] for x in bestFiltered])
        if bestFiltered+topArea > bestSoFar:
            bestSoFar = bestFiltered+topArea
    return bestSoFar

for i in range(numCases):
    n, k = inputF.readline().split()
    pancakes = []
    for j in range(int(n)):
        line = inputF.readline().strip().split()
        pancakes += [(int(line[0]), int(line[1]))]
    area = getMaxSurfaceArea(pancakes, int(k))

    output.write('Case #' + str(i+1) + ': ' + str(area) + '\n')
inputF.close()
output.close()
