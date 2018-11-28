#!/usr/bin/env python

from queue import PriorityQueue
import fileinput
import math
import sys

def g(N, K):
    divisor = 2 ** (math.ceil(math.log2(1 + K)) - 1)
    options = N - divisor + 1

    # Calculate division
    binsize = options // divisor

    # Calculate remainder
    remainder = options % divisor

    # At the partially occupied level, there are (divisor - remainder) bins of
    # size binsize and (remainder) bins of size binsize + 1

    # Calculate how many stalls on the partially occupied level will be occupied
    occupy = K - divisor + 1

    size = binsize
    if occupy > remainder:
        # In a bin of size binsize
        size = binsize
    else:
        # In a bin of size binsize + 1
        size = binsize + 1

    # Return nearest and farthest neighbours
    maxmin = math.floor((size - 1) / 2)
    maxmax = math.ceil((size - 1) / 2)

    return (maxmax, maxmin)

if __name__ == "__main__":
    case = 0

    for line in fileinput.input():
        line = line.rstrip()

        if case == 0:
            T = int(line)
        else:
            split = line.split(" ")
            N = int(split[0])
            K = int(split[1])

            maxmax, maxmin = g(N, K)

            print("Case #%d: %d %d" % (case, maxmax, maxmin))

        case += 1
