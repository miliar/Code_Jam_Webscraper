#!/usr/bin/env python3
"""
Cookie Clicker Alpha problem
for Google Code Jam 2014
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/2974486/dashboard#s=p1

author: 
Christos Nitsas
(chrisn654 or nitsas)

language:
Python 3(.3)

date:
April, 2014

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
import collections
import math
# non-standard modules:
from helpful import read_int, read_list_of_float


TestCase = collections.namedtuple("TestCase", ("C", "F", "X"))


def solve_test_case(tc):
    # I did the math and it turns out that the optimal number of farms 
    # to build is n* = X/C - 2/F - 1
    # - for n > n* farms it's faster if we build one less farm
    # - for n < n* it's facter if we build one more farm
    # - for n == n* it's the same if we build n and if we build n+1 farms
    # So, for the optimal strategy, we'll build either floor(n*) or ceil(n*) 
    # farms (whichever is better).
    n_star = tc.X/tc.C - 2/tc.F - 1
    if n_star < 0:
        # it's best if we build no farms
        return tc.X/2.0
    assert(tc.X > tc.C)
    n_floor = math.floor(n_star)
    n_ceil = math.ceil(n_star)
    time_to_build_n_floor_farms = 0
    for i in range(n_floor):
        time_to_build_n_floor_farms += tc.C/(2.0+i*tc.F)
    time_to_build_n_ceil_farms = time_to_build_n_floor_farms + tc.C/(2.0+n_floor*tc.F)
    time_with_n_floor_farms = time_to_build_n_floor_farms + tc.X/(2.0+n_floor*tc.F)
    time_with_n_ceil_farms = time_to_build_n_ceil_farms + tc.X/(2.0+n_ceil*tc.F)
    return min(time_with_n_floor_farms, time_with_n_ceil_farms)


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        T = read_int(f)
        test_cases = list(TestCase(*read_list_of_float(f)) for i in range(T))
    for i, tc in enumerate(test_cases, start=1):
        print("Case #{}: {:.7f}".format(i, solve_test_case(tc)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

