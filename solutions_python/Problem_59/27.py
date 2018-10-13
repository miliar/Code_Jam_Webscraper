#!/usr/bin/python

import sys

def line():
    return sys.stdin.readline()[:-1]

def readList():
    return map(eval,line().split())

if __name__ == '__main__':
    numberOfCases = eval(line())
    for caseNumber in range(numberOfCases):
        N,M = map(eval,line().split())
        existing = set()
        for i in range(N):
            newone = tuple(line().strip()[1:].split('/'))
            for j in range(len(newone)):
                existing.add(newone[:j+1])
        needed = 0
        for i in range(M):
            requested = tuple(line().strip()[1:].split('/'))
            for j in range(len(requested)):
                if requested[:j+1] not in existing:
                    needed += 1
                    existing.add(requested[:j+1])
        print "Case #" + str(caseNumber+1) + ": " + str(needed).replace('L',"")
