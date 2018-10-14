import math
from itertools import combinations
from collections import deque


def exposed(R, H):
    return (math.pi * R * R) + (2 * math.pi * R * H)

for i in range(int(raw_input())):
    N, K = map(int, raw_input().split())
    pancakes = list()
    for _ in range(N):
        R, H = map(int, raw_input().split())
        pancakes.append((R, H))

    options = list()
    for base in pancakes:
        _pancakes = pancakes[:]
        _pancakes.remove(base)
        _pancakes = [p for p in _pancakes if p[0] <= base[0]]
        _pancakes.sort(key=lambda p: -(p[0]*p[1]))
        _pancakes = _pancakes[:K-1]
        _pancakes.append(base)
        _pancakes.append((0, 0))

        sol = 0
        for j in xrange(len(_pancakes)):
            r, h = _pancakes[j]
            sol += (2 * math.pi * r * h)

        r, _ = _pancakes[-2]
        sol += (math.pi * r * r)
        options.append(sol)

    sol = max(options)



    # m = max(pancakes, key=lambda p: exposed(p[0], p[1]))
    #
    # pancakes.remove(m)
    # pancakes.sort(key=lambda p: -(p[0]*p[1]))
    # biggest = pancakes[:K-1]
    # biggest.append(m)
    # biggest.sort(key=lambda p: -p[0])
    #
    # biggest.append((0, 0))
    #
    # sol = 0
    # for j in xrange(len(biggest)):
    #     r, h = biggest[j]
    #     sol += (2 * math.pi * r * h)
    #
    # r, h = biggest[0]
    # sol += (math.pi * r * r)

    # sol = 0
    # for chosen in combinations(pancakes, K):
    #     r = 0
    #     cur = 0
    #     for R, H in chosen:
    #         r = max(r, R)
    #         cur += (2 * math.pi * R * H)
    #     cur += (math.pi * r * r)
    #
    #     if cur > sol:
    #         print chosen
    #         sol = max(sol, cur)

    print('Case #%d: %.9f' % (i+1, sol))
