#!/usr/bin/python
import sys
from math import pi
class AttDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

def processCase(case, caseNum):
    case.pancakes.sort(key=lambda x: x.ar, reverse=1)
    sol2 = case.pancakes[0].ar
    newPancakes = [x for x in case.pancakes[1:] if x.radius <= case.pancakes[0].radius]
    newPancakes.sort(key=lambda x: x.outer, reverse=1)
    sol2 += sum([x.outer for x in newPancakes[:case.stackSize-1]])
    case.pancakes.sort(key=lambda x: x.radius, reverse=1)
    sol1 = case.pancakes[0].ar
    newPancakes = case.pancakes[1:]
    newPancakes.sort(key=lambda x: x.outer, reverse=1)
    sol1 += sum([x.outer for x in newPancakes[:case.stackSize-1]])
    case.pancakes.sort(key=lambda x: x.ar, reverse=1)
    maxRad = max(sorted([x.radius for x in case.pancakes[:case.stackSize]]))
    sol3 = sum([x.outer for x in case.pancakes[:case.stackSize]]) + maxRad * maxRad * pi
    print("Case #%d: %.16f" % (caseNum, max([sol1, sol2, sol3])))

with open(sys.argv[1]) as f:
    data = f.read().split('\n')
    i = 0
    testCaseNum = int(data[i])
    i += 1
    testCases = []
    for _ in range(testCaseNum):
        numPancakes, stackSize = [int(x) for x in data[i].split(' ')]
        i += 1
        pancakes = []
        for _ in range(numPancakes):
            radius, height = [int(x) for x in data[i].split(' ')]
            i += 1
            dic = AttDict()
            dic.radius = radius
            dic.height = height
            dic.ar = radius * radius * pi + pi * radius * 2 * height
            dic.outer = pi * radius * 2 * height
            pancakes.append(dic)
        dic = AttDict()
        dic.numPancakes = numPancakes
        dic.stackSize = stackSize
        dic.pancakes = pancakes
        testCases.append(dic)
    caseNum = 0
    for case in testCases:
        caseNum += 1
        processCase(case, caseNum)
