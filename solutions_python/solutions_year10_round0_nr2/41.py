#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import fractions
import sys

def gcf(num, *others):
    for n in others:
        if num <= 1:
            break
        num = fractions.gcd(num, n)
    return num


def solve(*nums):
    minimum = min(nums)
    nums2 = [n-minimum for n in nums]
    gc = gcf(*(n for n in nums2 if n))
    return (gc-minimum) % gc


def main(filename):
    with open(filename, "r") as f:
        for case, line in enumerate(f):
            if not case:
                T = int(line.strip())
                continue
            if case > T:
                break
            line = [int(c) for c in line.split()][1:]
            print("Case #{0}: {1}".format(case, solve(*line)))


if __name__ == "__main__":
    main(sys.argv[1])
    sys.exit(0)

