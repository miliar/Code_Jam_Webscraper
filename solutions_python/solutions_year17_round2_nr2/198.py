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
    return readValues(int)


_OK = {"R": "BYG",
        "B": "RYO",
        "Y": "BRV",
        "O": "B",
        "G": "R",
        "V": "Y"
      }

_BASE = "RBY"

def solve(args):
    cnt = {}
    N, cnt["R"], cnt["O"], cnt["Y"], cnt["G"], cnt["B"], cnt["V"] = args

    first = [c for c in _BASE if cnt[c] > 0][0]
    prev = first
    ans = first
    cnt[first] -= 1

    for i in range(1, N):
        if cnt[_OK[prev][0]] > cnt[_OK[prev][1]]:
            prev = _OK[prev][0]
        else:
            prev = _OK[prev][1]
        cnt[prev] -= 1
        ans += prev

    if any(cnt[c] < 0 for c in _BASE) or not prev in _OK[first]:
        return 'IMPOSSIBLE'

    return ans

if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(readInput()))
