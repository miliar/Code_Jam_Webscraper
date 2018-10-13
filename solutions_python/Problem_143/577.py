#!/usr/bin/env python3
"""
New Lottery Game problem
for Google Code Jam 2014
Round 1B

Link to problem description:
https://code.google.com/codejam/contest/2994486/dashboard#s=p1

author: 
Christos Nitsas
(chrisn654 or nitsas)

language:
Python 3(.3)

date:
May, 2014

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
# non-standard modules:
from helpful import read_int, read_list_of_int


def solve(A, B, K):
    count = 0
    for ai in range(A):
        for bi in range(B):
            if ai & bi < K:
                count += 1
    return count


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        T = read_int(f)
        test_cases = [read_list_of_int(f) for i in range(T)]
    for i, tc in enumerate(test_cases, start=1):
        print("Case #{}: {}".format(i, solve(*tc)))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

