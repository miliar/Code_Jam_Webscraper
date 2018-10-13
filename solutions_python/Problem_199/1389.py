#!/usr/bin/env python3


def main():
    t = int(input())

    for x in range(1, t + 1):
        s, k = input().split(" ")
        y = calcNumFlips([c is "+" for c in s], int(k))
        print("Case #{}: {}".format(x, y))


def calcNumFlips(pancakes, flipperSize):
    flips = 0
    for i in range(0, len(pancakes) + 1 - flipperSize):
        if not pancakes[i]:
            flipAt(pancakes, i, flipperSize)
            flips += 1

    return flips if all(pancakes) else "IMPOSSIBLE"


def flipAt(pancakes, idx, flipperSize):
    for i in range(idx, idx + flipperSize):
        pancakes[i] = not pancakes[i]


main()
