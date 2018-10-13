__author__ = 'rutger'
import math

def calculateSurface(pancake):
    (radius, height) = pancake
    #print(math.pi * radius**2)
    return math.pi * radius**2


def calculateSkirt(pancake):
    (radius, height) = pancake
    #print(2 * radius * math.pi * height)
    return 2 * radius * math.pi * height


def calculateSquare(pancake):
    (radius, height) = pancake
    return math.pi * radius**2 + 2 * radius * math.pi * height


def solve2(n, beginIdx, k, pancakes, count, square):
    #print(n, beginIdx, k, pancakes, count, square)

    sq = square
    sq += calculateSkirt(pancakes[beginIdx])

    if count == 0:
        sq += calculateSurface(pancakes[beginIdx])

    cnt = count + 1
    if cnt == k:
        return sq
    pancakesLeft = n - beginIdx
    pancakesToChoose = k - cnt
    if pancakesLeft < pancakesToChoose:
        return -100.0

    maxSquare = -1000.0
    for i in range(beginIdx + 1, n):
        #print('test')
        tmp = solve2(n, i, k, pancakes, cnt, sq)
        #print(tmp)
        maxSquare = max(maxSquare, tmp)
    return maxSquare


def solve(n, k, pancakes):
    p = sorted(pancakes, reverse=True)
    maxIdx = n - k
    maxSquare = -1.0

    for i in range(maxIdx + 1):
        tmp = solve2(n, i, k, p, 0, 0.0)
        #print(tmp)
        maxSquare = max(maxSquare, tmp)
    return maxSquare




for T in range(int(input())):
    n, k = list(map(int, input().split(' ')))
    pancakes = []
    for i in range(n):
        radius, height = list(map(float, input().split(' ')))
        pancakes.append((radius, height))
    res = solve(n, k, pancakes)
    print('Case #%d: %f' % (T + 1, res))