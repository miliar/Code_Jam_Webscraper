#!/usr/bin/env python3
import math, collections, itertools
from sys import stdin


def readValue(valueType):
    return valueType(stdin.readline())


def readValues(valueType):
    return list(map(valueType, stdin.readline().split()))


class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def readInput():
    NC, NJ = readValues(int)
    AC = []
    for _ in range(NC):
        AC.append(readValues(int))
    AC.sort()
    AJ = []
    for _ in range(NJ):
        AJ.append(readValues(int))
    AJ.sort()

    if NJ > NC:
        return NJ, NC, AJ, AC
    return NC, NJ, AC, AJ


def solve(NC, NJ, AC, AJ):
    if NC == 1 and NJ == 0:
        return 2
    elif NC == 1 and NJ == 1:
        return 2
    else:
        if AC[1][1] - AC[0][0] > 720 and AC[0][1] + 1440 - AC[1][0] > 720:
            return 4
        return 2

    raise Error()

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
