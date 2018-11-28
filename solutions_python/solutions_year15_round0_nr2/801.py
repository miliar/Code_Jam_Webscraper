#! /usr/bin/python

import sys

def makeNewList(lst, itemToChange, newVal, valToAdd):
    res = []
    for k,x in enumerate(lst):
        if k == itemToChange:
            res.append(newVal)
        else:
            res.append(x)
    res.append(valToAdd)
    return res

def whichMax(lst):
    res = 0
    maxVal = lst[0]
    tmpLst = lst[1:]
    occs = 1
    for k,x in enumerate(tmpLst):
        if x > maxVal:
            res= k+1
            maxVal = x
            occs = 1
        if x == maxVal:
            occs += 1
    return res, maxVal, occs

def occurences(lst):
    """given an list, returns the number of occurences in that list for each disting element."""
    res = dict()
    for elt in lst:
        if elt in res.keys():
            res[elt] += 1
        else:
            res[elt] = 1
    return res

def newOccs(occs,valToChange, newVal1, newVal2):
    res = {}
    keys = occs.keys()
    for key in keys:
        if key != valToChange:
            if key not in res.keys():
                res[key] = occs[key]
            else:
                res[key] += occs[key]
        elif key == valToChange:
            val = occs[valToChange]
            if newVal1 in res.keys():
                res[newVal1] += val
            else:
                res[newVal1] = val
            if newVal2 in res.keys():
                res[newVal2] += val
            else:
                res[newVal2] = val
    return res

def calcMinTime(occs):
    vals = sorted(occs.keys(),reverse=True)
    maxVal = vals[0]
    n = occs[maxVal]
    if maxVal <= 3:
        return maxVal
    half = maxVal/2+1
    bestRes = maxVal
    for k in range(2,half):
        tmpOccs = newOccs(occs, maxVal, k,maxVal-k)
        tmpRes = n + calcMinTime(tmpOccs)
        if tmpRes < bestRes:
            bestRes = tmpRes
    return bestRes


def minTime2(pancakesDistr):
    occs = occurences(pancakesDistr)
    return calcMinTime(occs)
    

def minTime(pancakesDistr):
    maxPos, nMax, occs = whichMax(pancakesDistr)
    if nMax <= 3:
        return nMax
    if nMax == 4:
        if occs ==1:
            return 3
        return 4
    half = nMax/2+1
    bestRes = nMax
    for k in range(2,half):
        tmpDistr = makeNewList(pancakesDistr, maxPos, k, nMax-k)
        tmpRes = 1 + minTime(tmpDistr)
        if tmpRes < bestRes:
            bestRes = tmpRes
    return bestRes
    # nMaxFound = False
    # newPancakesDistr = []
    # half = nMax/2
    # for pancake in pancakesDistr:
    #     if not nMaxFound and pancake == nMax:
    #         newPancakesDistr.append(pancake - half)
    #         nMaxFound = True
    #     else:
    #         newPancakesDistr.append(pancake)
    # newPancakesDistr.append(half)
    # newPancakesDistr2 = []
    # for pancake in pancakesDistr:
    #     tmp = pancake - 1
    #     if tmp > 0:
    #         newPancakesDistr2.append(tmp)
    # return 1+min(minTime(newPancakesDistr),minTime(newPancakesDistr2)):
    


def getData(fileName):
    f = open(fileName,'r+')
    lines = [line for line in f]
    lines = map(lambda x:x.replace("\n",""),lines)
    nCases = int(lines[0])
    k = 1
    lines = lines[1:]
    while k <= nCases:
        
        d = int(lines[2*(k-1)])
        pancakes = lines[2*k-1]
        #print "case:",k,"pancakes =",pancakes
        pancakesDistr = sorted(map(int,pancakes.split(" ")),reverse=True)
        print "Case #"+str(k)+": "+str(minTime2(pancakesDistr))
        k = k+1


if __name__ == "__main__":
    fileName = sys.argv[1]
    getData(fileName)
