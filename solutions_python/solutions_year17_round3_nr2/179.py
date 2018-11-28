import sys
import math

def getInts():
    return list(map(int, input().split(" ")))

def getNLine( fnc, n ):
    return [ fnc() for y in range(n) ]

def getFloats():
    return list(map(float, input().split(" ")))

def solve(ac, aj, came, jami):
    came.sort(key=lambda x:x[0])
    jami.sort(key=lambda x:x[0])

    if ac==2:
        if (came[1][1] - came[0][0]<=720)  or (came[0][1] + 1440-came[1][0] <=720):
            ac = 1
    if aj==2:
        if (jami[1][1] - jami[0][0]<=720)  or (jami[0][1] + 1440-jami[1][0] <=720):
            aj = 1
    if ac == 2 or aj == 2:
        return 4

    else:
        return 2



T = int(input())
for i in range(T):
    [ac, aj] = getInts()
    came = getNLine(getFloats,ac)
    jami = getNLine(getFloats,aj)
    print('Case #{}: {}'.format(i + 1, solve(ac, aj, came, jami)))