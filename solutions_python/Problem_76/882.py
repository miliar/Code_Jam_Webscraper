#!/usr/bin/env python
from collections import deque
from exceptions import Exception
from copy import copy
from itertools import combinations

def get_input():
    from sys import stdin
    input = stdin.readlines()
    return input[0], deque(input[1:])

def xor_list(list):
    result = list[0]
    if len(list) > 1:
        for i in list[1:]:
            result = result ^ i
    return result

def split_candies(candies):
    result = 0

    for n in xrange(1, len(candies)):
        for setB in combinations(candies, n):
            setA = copy(candies)
            for i in setB:
                setA.remove(i)

            if xor_list(setA) == xor_list(setB):
                sumA = sum(setA)
                if sumA > result: result = sumA

    if result > 0:
        return result
    else:
        return "NO"

if __name__ == "__main__":
    cases, data = get_input()

    for case in range(int(cases)):
        candies_size = int(data.popleft())
        candies = [ int(c) for c in data.popleft().split() ]
        if candies_size == len(candies):
            print("Case #%s: %s" % (case+1, split_candies(candies)))
        else:
            raise Exception("Invalid number of candies")
