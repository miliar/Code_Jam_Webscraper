#!/usr/bin/env python

import sys
from heapq import *

def parseTime(x):
    x = x.split(':')
    return int(x[0])*60 + int(x[1])


def doTrains(schedule, trains):
    if trains and trains[0] <= schedule[0]:
        heappop(trains)
        return 0
    else:
        return 1


def solve(T, A, B):
    trainsA = []
    trainsB = []
    nA, nB = 0, 0

    A.sort()
    B.sort()
    A = list(reversed(A))
    B = list(reversed(B))

    while A or B:
        if not B or (A and A[-1] < B[-1]):
            schedule = A.pop()
            nA += doTrains(schedule, trainsA)
            heappush(trainsB, schedule[1] + T)
        else:
            schedule = B.pop()
            nB += doTrains(schedule, trainsB)
            heappush(trainsA, schedule[1] + T)

    return (nA,nB)


readline = lambda : sys.stdin.readline().strip()

N = int(readline())

for n in range(N):
    T = int(readline())
    NA, NB = map(int, readline().split())
    A = []
    B = []
    for na in range(NA):
        A.append(map(parseTime, readline().split()))
    for nb in range(NB):
        B.append(map(parseTime, readline().split()))

    print "Case #%d: %d %d" % ((n+1,) + solve(T, A, B))
