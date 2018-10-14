#!/usr/bin/env python

import sys

def solve(N, K):
    rsnaps = req_snaps(N)
    if K < rsnaps:
        return "OFF"
    elif K == rsnaps:
        return "ON"
    elif K > rsnaps:
        if (K + 1) % (rsnaps + 1) == 0:
            return "ON"
        else:
            return "OFF"

def req_snaps(N):
    if N < 2:
        return 1
    return req_snaps(N - 1) * 2 + 1


def main(filename):
    f = open(filename, 'r')
    num_cases = int(f.readline())
    for i in range(num_cases):
        N, K = [int(e) for e in f.readline().split()]
        status = solve(N, K)
        print "Case #%i: %s" % (i + 1, status)

    f.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Please specify the input file!")
    main(sys.argv[1])
