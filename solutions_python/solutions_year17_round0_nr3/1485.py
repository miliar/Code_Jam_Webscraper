#!/usr/bin/env python3
import math
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
    return readValues(int)


def solve(N, K):
    logK = int(math.log2(K))
    remainder = N - 2 ** logK + 1
    divSize = remainder // (2 ** logK)
    extra = remainder - 2 ** logK * divSize

    if K - 2 ** logK < extra:
        divSize += 1

    return str(divSize // 2) + " " + str((divSize - 1) // 2)


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))