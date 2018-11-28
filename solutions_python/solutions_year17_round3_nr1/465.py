#! /usr/bin/env python3

import os
import os.path
import argparse
import sys
import math
import copy
from pprint import pprint


def solve(testcase, f):
    N, K = [int(x) for x in f.readline().split(" ")]
    available = []
    for i in range(N):
        # Ri: radius, Hi: height
        available.append([int(x) for x in f.readline().split(" ")])

    available.sort(key = lambda x: -(x[0] * x[1]))

    # Max area on side
    max_area = 0

    for i in range(N):
        max_r = 0
        p = available[i]
        area = 2 * p[0] * p[1]
        max_r = max(max_r, p[0])

        num = 1
        j = 0
        while num < K:
            if j == i:
                j += 1
                continue
            p = available[j]
            num += 1
            j += 1
            area += 2 * p[0] * p[1]
            max_r = max(max_r, p[0])
        area += max_r ** 2
        max_area = max(max_area, area)

    answer = math.pi * max_area
    print("Case #{} Input: {} available, {} requested".format(testcase, N, K))
    print("Output: {}".format(answer))
    fout.write("Case #{}: {:.6f}\n".format(testcase, answer))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help='Filename')

    args = parser.parse_args()

    outputfile = os.path.splitext(args.filename)[0] + ".out"

    with open(args.filename, 'r') as f:
        with open(outputfile, 'w+') as fout:
            num_tests = int(f.readline().strip())
            for testcase in range(1,num_tests+1):
                solve(testcase, f)

