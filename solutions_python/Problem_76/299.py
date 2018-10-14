import os, sys
from math import *

def add_binary(sequence, start, end):
    result = sequence[start]
    for i in range(start + 1, end + 1):
        result = result ^ sequence[i]
    return result

def add(sequence, start, end):
    result = sequence[start]
    for i in range(start + 1, end + 1):
        result = result + sequence[i]
    return result


def solve(piles):
    #if add_binary(piles, 0, len(piles) - 1) != 0:
    #    return 'NO'
    piles.sort()
    binary = piles[0]
    other_binary = add_binary(piles, 1, len(piles) - 1)
    for i in range(0, len(piles) - 1):
        if binary == other_binary:
            return add(piles, i + 1, len(piles) - 1)
        binary = binary ^ piles[i]
        other_binary = other_binary ^ piles[i]
    return 'NO'   

nCases = int(sys.stdin.readline())

for case in range(1, nCases + 1):
    length = int(sys.stdin.readline())
    args = map(int, sys.stdin.readline().split())
    piles = args[0:length]
    print "Case #" + str(case) + ": " + str(solve(piles))
