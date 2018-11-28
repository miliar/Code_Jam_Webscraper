#!/usr/bin/python

import sys

def solve(line):
    num_stand = 0
    min_stand = 0
    line = line.split()
    max_shy = int(line[0].strip())
    aud = [int(ch) for ch in list(line[1].strip())]
    for i, num in enumerate(aud):
        if i==0:
            num_stand += num
        else:
            if num_stand >= i:
                num_stand += num
            else:
                min_stand += (i-num_stand)
                num_stand += (i-num_stand+num)
    return min_stand


def main(filename):
    with open(filename, "r") as f:
        for case, line in enumerate(f):
            if not case:
                T = int(line.strip())
                continue
            if case > T:
                break
            print("Case #{0}: {1}".format(case, solve(line)))


if __name__ == "__main__":
    main(sys.argv[1])
    sys.exit(0) 