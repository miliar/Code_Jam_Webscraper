#!/usr/bin/python
import os, sys
import operator, math

def distSqr(x, y):
    return (x[0] - y[0]) * (x[0] - y[0]) + (x[1] - y[1]) * (x[1] - y[1])

def findSprinkler(plants):
    plants = list(plants)
    if (len(plants) == 0):
        return 0
    elif (len(plants) == 1):
        # radius of one plant
        return plants[0][2]
    # Otherwise, find the center of mass.
    minX = min([p[0] for p in plants])
    maxX = max([p[0] for p in plants])
    minY = min([p[1] for p in plants])
    maxY = max([p[1] for p in plants])
    x = (minX + maxX) / 2.0
    y = (minY + maxY) / 2.0
    # small case, only need to handle 2!
    radiusDiff = 0
    enclosed = False
    if (len(plants) == 2):
        bigPlant = 0
        if plants[1][2] > plants[0][2]:
            bigPlant = 1
        if bigPlant == 0:
            radiusDiff = plants[0][2] - plants[1][2]
        else:
            radiusDiff = plants[1][2] - plants[0][2]
        # Check for enclosure
        smallPlant = 1 - bigPlant
        #print smallPlant
        #print bigPlant
        math.sqrt(distSqr(plants[bigPlant], plants[smallPlant]))
        if math.sqrt(distSqr(plants[bigPlant], plants[smallPlant])) + plants[smallPlant][2] <= plants[bigPlant][2]:
            enclosed = True
            return plants[bigPlant][2]

    # now find the max radius
    radius = 0
    for p in plants:
        d = math.sqrt(distSqr([x,y], p)) + p[2]
        if d > radius:
            radius = d
    radius -= radiusDiff/2.0
    # Need to adjust based on radius
    maxPlantRadiusIdx = max([plants[i][2] for i in range(len(plants))])
    return radius


def findSprinklers(plants1, plants2):
    r1 = findSprinkler(plants1)
    r2 = findSprinkler(plants2)
    return max(r1, r2)

def findMinRadius(plants):
    # Bruuuute force time!
    # All possible splits
    minRadius = float('Inf')
    for [p1, p2] in split(range(len(plants))):
        #print p1
        if len(p1) <= 2 and len(p2) <= 2:
            val = findSprinklers([plants[x] for x in list(p1)], [plants[x] for x in list(p2)])
            if val < minRadius:
                minRadius = val
    return minRadius




def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        numPlants = int(fileLines[index][:-1])
        index += 1
        plants = [[] for x in xrange(numPlants)]
        for i in xrange(numPlants):
            plants[i] = [int(x) for x in fileLines[index][:-1].split(' ')]
            index += 1
        #print plants
        mr = findMinRadius(plants)
        #print [x for x in split([x for x in range(len(plants))])]
        print "Case #%d: %.9f" % (caseNum+1, mr)


def split(x):
    """ Generate splits of x into two things """
    if len(x) == 0:
        yield [[], []]
        return
    for [s1, s2] in split(x[1:]):
        yield [[x[0]] + s1, s2]
        yield [s1, [x[0]] + s2]

if __name__ == '__main__':
    main(sys.argv[1])
