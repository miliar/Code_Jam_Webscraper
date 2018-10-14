#!/user/bin/env python -tt

import sys
import os

def createEntry(myDict, myList):
    item = myList.pop(0)
    if item not in myDict:
        myDict[item] = {}
    if len(myList) == 0:
        return
    createEntry(myDict[item], myList)
    return

def addEntry(myDict, myList):
    item = myList[0]
    if item in myDict:
        myList.pop(0)
        if len(myList) == 0:
            return 0
        return addEntry(myDict[item], myList)
    nrOfPaths = len(myList)
    createEntry(myDict, myList)
    return nrOfPaths
    

T = int(sys.stdin.readline())

for t in xrange(1, T+1):
    print 'Case #%d:' % t,
    N, M = map(int, sys.stdin.readline().split())
    paths = {}
    line = []
    for n in xrange(N):
        line = sys.stdin.readline().lstrip('/').rstrip().split('/')
        createEntry(paths, line)
    count = 0
    for m in xrange(M):
        line = sys.stdin.readline().lstrip('/').rstrip().split('/')
        count += addEntry(paths, line)
    print count
