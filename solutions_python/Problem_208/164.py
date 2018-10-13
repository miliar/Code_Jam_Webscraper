#!/usr/bin/env pypy3
"""Task #3"""

for case in range(1, int(input()) + 1):



    num = int(input().split()[0])
    cities = [] #dist, speed
    for _ in range(num):
        cities.append([int(x) for x in input().split()])
    dists = []
    for i in range(num - 1):
        dists.append(int(input().split()[i + 1]))

    input()
    input()

    currpos = 0
    queue = [(0, cities[0][0], cities[0][1])] # time, distleft, speed
    while currpos < num - 1:
        contqueue, changequeue = [], []
        while queue:
            curr = queue.pop()
            distleft = curr[1] - dists[currpos]
            if distleft < 0:
                continue
            time = curr[0] + dists[currpos] / curr[2]
            contqueue.append([time, distleft, curr[2]])
            changequeue.append([time, cities[currpos+1][0], cities[currpos+1][1]])
        bestchange = min(changequeue)
        queue = contqueue + [bestchange]
        currpos += 1
    best = min(queue)
    result = best[0]






    print('Case #{}: {}'.format(str(case), str(result)))
