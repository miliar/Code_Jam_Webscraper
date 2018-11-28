#!/usr/bin/python

__author__ = 'sbuono'

import sys

def minutesToFinish(nbPan) :

    p = 0
    max = 0
    maxi = 0
    while p < len(nbPan) :
        i = 0
        while i < len(nbPan[p]) :
            if int(nbPan[p][i]) > max :
                max = int(nbPan[p][i])
                maxi = i
            i += 1
        p += 1
    return max

def allOnes( nbPan) :

    for p in nbPan :
        for i in p :
            if int(i) > 1 :
                return False
    return True

def getMaxI(nbPan) :
    p = 0
    max = 0
    maxi = 0
    while p < len(nbPan) :
        i = 0
        while i < len(nbPan[p]) :
            if int(nbPan[p][i]) > max :
                max = int(nbPan[p][i])
                maxi = p
            i += 1
        p += 1
    return maxi

def getTot(l) :
    tot = 0
    for i in l :
        tot += int(i)
    return tot

f = open(sys.argv[1])

nbTestCases = int(f.readline().strip())

case = 1

lines = f.readlines()

for i in range(0, len(lines), 2) :

    nbDiners = int(lines[i].strip())
    nbPan = lines[i+1].strip().split()

    list = []
    for d in nbPan :
        list.append([d])
    nbPan = list

    nbTotMin = minutesToFinish(nbPan)

    nbSpecMin = 0
    while not allOnes(nbPan) and nbSpecMin < nbTotMin :
        nbSpecMin += 1

        max = getMaxI(nbPan)

        nbToSplit = len(nbPan[max]) + 1
        tot = getTot(nbPan[max])
        nbPan[max] = []
        splitNb = int(tot / nbToSplit)

        tmp = 0
        while nbToSplit > 1 :
            nbPan[max].append(splitNb)
            tmp += splitNb
            nbToSplit -= 1
        nbPan[max].append(tot - tmp)

        newMin = minutesToFinish(nbPan)

        if nbSpecMin + newMin < nbTotMin :
            nbTotMin = nbSpecMin + newMin


    print "Case #%d: %d" % (case, nbTotMin)

    case += 1