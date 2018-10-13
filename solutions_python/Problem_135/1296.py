#!/usr/bin/env python
# vim: set filetype=python et sw=4 ts=4:

import sys

def solve_case(row1, row2):
    intersection = set(row1) & set(row2)
    if 1 == len(intersection):
        sys.stdout.write(str(intersection.pop()))
    elif len(intersection) == 0:
        sys.stdout.write("Volunteer cheated!")
    else:
        sys.stdout.write("Bad magician!")

T = int(sys.stdin.readline())

def get_row(stream):
    row = int(stream.readline())
    for x in xrange(row-1):
        stream.readline()
    result = [int(x) for x in stream.readline().split()]
    for x in xrange(4 - row):
        stream.readline()
    return result

for case in xrange(T):
    row1 = get_row(sys.stdin)
    row2 = get_row(sys.stdin)
    sys.stdout.write("Case #%d: " % (case + 1))
    solve_case(row1, row2)
    sys.stdout.write("\n")
