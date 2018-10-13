#!/usr/bin/env python3

import math


def main():
    t = int(input())

    for x in range(1, t + 1):
        N, K = map(int, input().split(" "))
        pancakes = []
        for z in range(0, N):
            R, H = map(int, input().split(" "))
            pancakes.append({'R': R, 'H': H})
        y = getSurface(K, pancakes)
        print("Case #{}: {}".format(x, y))


def getSurface(K, pancakes):
    for p in pancakes:
        p['S'] = sideSurface(p)
        p['T'] = topSurface(p)
        p['total'] = p['T'] + p['S']

    if len(pancakes) == K:
        return stackSurface(pancakes)

    pancakes.sort(key=lambda p: p['S'], reverse=True)

    if 1 == K:
        return stackSurface([max(pancakes, key=lambda p: p['total'])])

    topS = pancakes[:K-1]
    flopS = pancakes[K-1:]
    maxR = max(topS, key=lambda p: p['R'])
    baseAlternatives = [p for p in flopS if p['R'] >= maxR['R']]
    configs = [topS + [flopS[0]]]

    if baseAlternatives:
        altBase = max(baseAlternatives, key=lambda p: p['total'])
        configs.append([altBase] + topS)

    return max(map(stackSurface, configs))


def stackSurface(s):
    maxR = max(s, key=lambda p: p['R'])
    s.remove(maxR)
    return sum([p['S'] for p in s]) + maxR['total']


def topSurface(p):
    return math.pi * p['R'] ** 2


def sideSurface(p):
    return 2 * math.pi * p['R'] * p['H']


main()
