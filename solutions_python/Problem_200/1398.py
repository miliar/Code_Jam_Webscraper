#! /usr/bin/env python

import sys


def solve(line):
    if len(line) == 1:
        return line
    prev = "0"
    for i, digit in enumerate(line):
        if digit < prev:
            left_part = str(int(line[:i])-1)
            right_part = "9" * (len(line) - i)
            return solve(left_part + right_part)
        prev = digit
    return int(line)


if __name__ == "__main__":
    with file(sys.argv[1]) as f:
        cases = int(f.readline())
        for i in range(cases):
            line = f.readline().strip()
            print("Case #%d: %s" % (i+1, solve(line)))