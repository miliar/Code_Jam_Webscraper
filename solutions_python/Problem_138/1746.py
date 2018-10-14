#!/usr/bin/env python
tc = int(input())

def calcDW(naomiB, kenB, nrB):
    pts = 0
    kenB = kenB
    while nrB > 0:
        nBA = naomiB.pop(0)

        if nBA > kenB[0] :
            nBA = kenB[-1]+0.000001
        elif nrB > 1 and nBA < kenB[-1]:
            nBA = kenB[-2]+0.000001

        kenScored = False
        for kb in kenB:
            if kb > nBA:
                kenB.remove(kb)
                kenScored = True
                break
        if not kenScored:
            kenB = kenB[1:]
            pts += 1
        nrB = nrB-1
    return pts

def calcW(naomiB, kenB, nrB):
    pts = 0
    while nrB > 0:
        nBA = naomiB.pop(0)
        kenScored = False
        for kb in kenB:
            if kb > nBA:
                kenB.remove(kb)
                kenScored = True
                break
        if not kenScored:
            kenB = kenB[1:]
            pts += 1
        nrB = nrB-1
    return pts

for t in range(tc):
    nrB = float(input())
    naomiB = sorted(list(map(float, input().split())))
    kenB = sorted(list(map(float, input().split())))
    resDW = calcDW(naomiB[:], kenB[:], nrB)
    resW = calcW(naomiB[:], kenB[:], nrB)
    print("Case #" + str(t+1) + ":", str(resDW), str(resW) )