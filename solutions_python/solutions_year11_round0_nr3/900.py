#!/usr/bin/env python

import operator


def calcPatrick(v1, v2):
    return v1 ^ v2

seanRealList = []

def dfs(candies, patrick, sean, seanReal):
#    print "patrick : " + str(patrick)
#    print "sean : " + str(sean)
#    print "seanReal : " + str(seanReal)
#    print "seanList : " + str(seanRealList)
    if len(candies) == 0:
        if patrick == sean:
            seanRealList.append(seanReal)
#            print seanReal
        return
    else:
        dfs(candies[1:], patrick ^ candies[0], sean, seanReal)
        dfs(candies[1:], patrick, sean ^ candies[0], seanReal + candies[0])

f = open("C-small-attempt0.in")
testNum = int(f.readline())

for iTest in range(0, testNum):
    f.readline()
    candies = map(int, f.readline().split())
    sum = reduce(operator.add, candies)
#    print "candies : " + str(candies)
    if (sum % 2 == 1):
        print "Case #" + str(iTest+1) + ": NO"
        continue

    seanRealList = []
    results = dfs(candies, 0, 0, 0)
    seanRealList.sort()
#    print "result : " + str(seanRealList)
    if len(seanRealList) == 0:
        print "Case #" + str(iTest+1) + ": NO"
    elif seanRealList[-1] == sum:
        print "Case #" + str(iTest+1) + ": " + str(seanRealList[-2])
    else:
        print "Case #" + str(iTest+1) + ": " + str(seanRealList[-1])

f.close()
