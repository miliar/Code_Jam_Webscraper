#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import operator
import sys

def solve(line):
    places = 0
    for i, x in enumerate(line.split()):
        if int(x) - i != 1:
            places += 1
    return str(places) + '.000000'
    

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

