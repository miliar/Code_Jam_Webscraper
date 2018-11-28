#!/usr/bin/python
import os, sys, math

def solve(farmCost, farmCookies, win):
    COOKIES_PER_SEC = 2.0
    # if farms give less/the same as this, it's easy
    #if farmCookies <= COOKIES_PER_SEC:
    #    return win/COOKIES_PER_SEC
    # breakeven point is (FX-2*C)/(FC)
    breakevenFarmNum = (farmCookies*win - COOKIES_PER_SEC*farmCost)/(farmCookies*farmCost)
    #print breakevenFarmNum
    if breakevenFarmNum < 1.0:
        return win/COOKIES_PER_SEC
    numFarms = math.floor(breakevenFarmNum)
    time = 0.0
    for i in range(int(numFarms)):
        # have i farms so far
        time += farmCost/(COOKIES_PER_SEC + i*farmCookies)
    time += win/(COOKIES_PER_SEC + numFarms*farmCookies)
    return time

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        [farmCost, farmCookies, win] = [float(x) for x in fileLines[index][:-1].split()]
        index += 1
        answer = solve(farmCost, farmCookies, win)
        #print caseStr
        print "Case #%d: %.7f" % (caseNum + 1, answer)

if __name__ == '__main__':
    main(sys.argv[1])
