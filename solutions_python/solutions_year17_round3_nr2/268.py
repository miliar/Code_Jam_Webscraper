#! /bin/python

from sys import stdin
from math import inf

def findMinJoin(duration, letter):

    minI = -1;
    minD = inf;

    for i in range(len(duration)):
        (d, l) = duration[i]
        if l == 'f' and duration[i-1][1] == letter and duration[i-1][1] == letter:
            if d < minD:
                minI = i
                minD = d

    if minI != -1:
        return minI



T = int(stdin.readline())

for t in range(T):

    [AC, AJ] = [int(x) for x in stdin.readline().split()]

    # timeline = []
    # timeJ = 12 * 60
    # timeC = 12 * 60
    # for _ in range(AC):
    #     [C, D] = [int(x) for x in stdin.readline().split()]
    #     timeline.append((C, D, 'C'))
    #     timeJ -= D - C

    # for _ in range(AJ):
    #     [C, D] = [int(x) for x in stdin.readline().split()]
    #     timeline.append((C, D, 'J'))
    #     timeC -= D - C

    # timeline.sort()
    # duration = []
    # lastTime = 0
    # lastLetter = ''

    # for (c, d, l) in timeline:
    #     if c == lastTime:
    #         if l == lastLetter:
    #             duration[-1][0] += d - c
    #         else:
    #             duration.append((d - c, l))
    #     else:
    #         duration.append((c - lastTime, 'f'))
    #         duration.append((d - c, l))
    #     lastLetter = l
    #     lastTime = d

    # if timeline[0][0] != timeline[-1][1]:
    #     duration.append((timeline[0][0] + 24*60 - timeline[-1][1], 'f'))

    # # Greedy strategy : search for the minimal joinable intervals and
    # # merge them
    # i = findMinJoin(duration, 'C')
    # while i != None:
    #     if duration[i][1] < timeJ:
    #         d = duration[i] + duration[(i+1)%len(duration)][0] + duration[i-1][0]
    #         duration[i] = (d, 'C')
    #         timeJ -= duration[i][0]
    #     else:
    #         break
    #     i = findMinJoin(duration, 'C')

    # i = findMinJoin(duration, 'J')
    # while i != None:
    #     if duration[i][1] < timeC:
    #         d = duration[i][0] + duration[(i+1)%len(duration)][0] + duration[i-1][0]
    #         duration[i] = (d, 'J')
    #         timeC -= duration[i][0]
    #         indices = duration[(i+1)%len(duration)][0], duration[i-1][0]
    #         duration = [i for j, i in enumerate(somelist) if j not in indices]
    #     else:
    #         break
    #     i = findMinJoin(duration, 'J')

    # res =

    # Small case

    CAct = []
    JAct = []

    for _ in range(AC):
        [C, D] = [int(x) for x in stdin.readline().split()]
        CAct.append((C, D))

    for _ in range(AJ):
        [C, D] = [int(x) for x in stdin.readline().split()]
        JAct.append((C, D))

    res = 2
    if len(JAct) == 2:
        tt = max(JAct[0][1], JAct[1][1]) - min(JAct[0][0], JAct[1][0])
        tt2 = 24 * 60 - max(JAct[0][0], JAct[1][0]) + min(JAct[0][1], JAct[1][1])
        tt = min(tt, tt2)
        if tt > 12 * 60:
            res = 4
    elif len(CAct) == 2:
        tt = max(CAct[0][1], CAct[1][1]) - min(CAct[0][0], CAct[1][0])
        tt2 = 24 * 60 - max(CAct[0][0], CAct[1][0]) + min(CAct[0][1], CAct[1][1])
        tt = min(tt, tt2)
        if tt > 12 * 60:
            res = 4

    print("Case #{}: {}".format(t+1, res))
