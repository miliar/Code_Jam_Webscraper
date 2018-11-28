import sys
from itertools import combinations

lines = sys.stdin.read().split("\n")
count = lines[0]

index = 1
for line in lines[1:-1]:
    s = map(int, line.split())
    regular = {}
    surprising = {}
    N, S, p, T = s[0], s[1], s[2], s[3:]
    for i in range(N):
        z = T[i]
        y = z / 3
        if z == 0:
            regular[i] = (0,0,0)
            surprising[i] = None
        elif z == 1:
            regular[i] = (0,0,1)
            surprising[i] = None
        elif z == 29:
            regular[i] = (9,10,10)
            surprising[i] = None
        elif z == 30:
            regular[i] = (10,10,10)
            surprising[i] = None
        elif z % 3 == 0:
            regular[i] = (y, y, y)
            surprising[i] = (y - 1, y, y +1)
        elif z % 3 == 1:
            regular[i] = (y, y, y + 1)
            surprising[i] = (y - 1, y + 1, y +1)
        else:
            regular[i] = (y, y+1, y+1)
            surprising[i] = (y, y, y+2)
    good = [x for x in surprising.keys() if surprising[x]]
    count = 0
    highest = 0
    for surprise in combinations(good, S):
        tmp = 0
        for m in range(N):
            if m in surprise:
                if surprising[m][2] >= p:
                    tmp += 1
            elif regular[m][2] >= p:
                tmp += 1
        if tmp > highest:
            highest = tmp
    print "Case #%d: %d" % (index, highest)
    index += 1
