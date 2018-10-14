
import sys
from math import *


def is_even(value):
    return value % 2 == 0


T = int(sys.stdin.readline())

for i in range(0, T):
    tokens = sys.stdin.readline().strip().split()
    N = int(tokens[0])
    K = int(tokens[1])
    level = int(floor(log(K, 2)))
    previousOnLevel = K - 2**level

    counts = {N: 1}  # Formatted as (amount, distance)
    for j in range(0, level):
        newCounts = {}
        for d, a in counts.items():
            if is_even(d):
                factors = [d/2 - 1, d/2]
            else:
                factors = [(d - 1)/2, (d - 1)/2]
            for factor in factors:
                newCounts.setdefault(factor, 0)
                newCounts[factor] += a
        counts = newCounts

    counts = sorted(counts.items(), reverse=True)

    index = 0
    while True:
        previousOnLevel -= counts[index][1]
        if previousOnLevel < 0:
            break
        index += 1

    distance = counts[index][0]
    if is_even(distance):
        factors = [distance / 2 - 1, distance / 2]
    else:
        factors = [(distance - 1) / 2]

    print("Case #%d: %d %d" % ((i+1), max(factors), min(factors)))