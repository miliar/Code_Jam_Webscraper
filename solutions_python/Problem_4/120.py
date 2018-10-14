#!/usr/bin/python
import sys

if __name__ == '__main__':
    next = sys.stdin.readline
    numberOfCases = int(next())
    for caseNumber in range(1,numberOfCases+1):
        n = int(next())
        v = map(int,next().split())
        u = map(int,next().split())
        u.sort()
        v.sort()
        v.reverse()
        acum = 0
        for i in range(0,n):
            acum = acum + u[i]*v[i]

        print "Case #" + str(caseNumber) + ": " + str(acum)
