import sys
from collections import *
sn = sys.stdin

def transpose(field):
    return [[field[y][x] for y in range(len(field))]
                        for x in range(len(field[0]))]

T = int(sn.readline())
for icase in range(T):
    N, M = map(int, sn.readline().split())
    field = []
    for y in range(N):
        field.append(map(int, sn.readline().split()))
    yproj = map(max, field)
    xproj = map(max, transpose(field))

    re = True
    for y in range(len(field)):
        for x in range(len(field[0])):
            here = field[y][x]
            if here >= yproj[y] or here >= xproj[x]:
                pass
            else:
                re = False

    print "Case #%d:" % (icase+1), ("YES" if re else "NO")
    
