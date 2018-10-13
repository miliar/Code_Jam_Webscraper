#!/usr/bin/python
import os, sys, math

# cache((pos, holdingVine))
cache = {}

def canVineCrawl(vines, D, pos, holdingVine):
    global cache
    #print (pos, holdingVine)
    thisKey = (pos, holdingVine)
    if thisKey in cache:
        return cache[thisKey]
    if pos >= D:
        cache[thisKey] = True
        return True
    vineDist = min(vines[holdingVine][0]-pos, vines[holdingVine][1])
    # See which vines we can grab
    #print vineDist, D
    maxVineDist = vines[holdingVine][0] + vineDist 
    #print maxVineDist
    possibleVines = []
    if maxVineDist >= D:
        cache[thisKey] = True
        return True
    for i in range(holdingVine+1, len(vines)):
        if (vines[i][0] <= maxVineDist):
            possibleVines.append(i)
        else:
            break
    #print possibleVines
    if len(possibleVines) == 0:
        cache[thisKey] = False
        return False
    for i in possibleVines:
        distanceToVine = vines[i][0] - vines[holdingVine][0]
        #newPos = vines[i][1] - min(distanceToVine, vines[i][1])
        #newPos = vines[i][0] - min(distanceToVine, vines[i][1])
        newPos = vines[i][0] - min(distanceToVine, vines[i][1], vines[holdingVine][1])
        key = (newPos, i)
        if (newPos, i) in cache:
            if cache[(newPos, i)] == True:
                cache[thisKey] = True
                return True
            else:
                continue
        # have to calculate
        canCrawl = canVineCrawl(vines, D, newPos, i)
        if canCrawl:
            cache[thisKey] = True
            return True
    # couldn't do it
    cache[thisKey] = False
    return False

def main(filename):
    global cache
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        numVines = int(fileLines[index][:-1])
        index += 1
        vines = []
        for i in range(numVines):
            caseStr = fileLines[index][:-1]
            vines.append([int(x) for x in caseStr.split(' ')])
            index += 1
        D = int(fileLines[index][:-1])
        index += 1
        cache = {}
        #print vines
        canDo = canVineCrawl(vines, D, 0, 0)
        print "Case #%d: %s" % (caseNum + 1, 'YES' if canDo else 'NO')

if __name__ == '__main__':
    main(sys.argv[1])
