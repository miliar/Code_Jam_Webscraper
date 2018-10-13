#!/bin/python3


def flip(c):
    if c == "+":
        return "-"
    else:
        return "+"


def flipCount(cakes, flipK):
    if "-" not in cakes:
        return 0
    elif len(cakes[cakes.index("-"):]) < flipK:
        return "IMPOSSIBLE"
    else:
        newCakes = cakes[cakes.index("-"):]
        for i in range(flipK):
            newCakes[i] = flip(newCakes[i])
        # print(str(newCakes))
        nextMoves = flipCount(newCakes, flipK)
        if nextMoves == "IMPOSSIBLE":
            return "IMPOSSIBLE"
        else:
            return nextMoves + 1

T = int(input().strip())
for test in range(T):
    cakes, flipK = input().split()
    cakes = list(cakes)
    flipK = int(flipK)
    flips = str(flipCount(cakes, flipK))
    print('Case #%d: %s' % ((test + 1), flips))
