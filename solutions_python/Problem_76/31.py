#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import operator
import sys

def solve(line):
    line = map(int, line.split())
    if reduce(operator.xor, line):
        return "NO"
    else:
        return sum(line) - min(line)


def main(filename):
    with open(filename, "r") as f:
        for case, line in enumerate(f):
            if not case:
                T = int(line.strip())
                continue
            if line:
                if not case % 2:
                    print("Case #{0}: {1}".format(case // 2, solve(line)))


if __name__ == "__main__":
    main(sys.argv[1])
    sys.exit(0)

