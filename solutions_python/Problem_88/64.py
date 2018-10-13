#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Round 2 Problem B
Author: Matt Giuca
"""

import sys

### Input parsing ###

def parse_input(infile):
    """Consume input for a single case from infile.
    Return or yield a data structure describing the input.
    """
    r, c, d = tuple(map(int, infile.readline().split()))
    ws = []
    for i in range(r):
        row = infile.readline().strip()
        assert len(row) == c
        ws.append(row)
    return r, c, d, ws

### Algorithm ###

def com_ok(ws, x, y, k):
    expect_com = x + (k/2), y + (k/2)
    #print("centre_of_mass({0}, {1}, {2}) = {3}?".format(x, y, k, expect_com))
    sx, sy = 0, 0
    for j in range(y, y+k):
        for i in range(x, x+k):
            if ((i == x and j == y) or (i == x and j == y+k-1)
                or (i == x+k-1 and j == y) or (i == x+k-1 and j == y+k-1)):
                continue
            #print("    ({0}, {1})".format(i+0.5, j+0.5))
            massp = ws[j][i]
            sx += (i+0.5 - expect_com[0]) * massp
            sy += (j+0.5 - expect_com[1]) * massp
    return abs(sx - 0) < 0.000001 and abs(sy - 0) < 0.000001

def handle_case(data):
    """Given the data structure returned by parse_input, return the answer as
    a string or stringable value.
    If parse_input is a generator, should manually call list() on data.
    """
    r, c, d, ws = data
    ws = [[int(c)+d for c in row] for row in ws]
    for k in range(min(r, c), 2, -1):
        for y in range(r-k+1):
            for x in range(c-k+1):
                if com_ok(ws, x, y, k):
                    return k
    return None

### Top-level ###

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}: {1}".format(casenum+1,
            answer if answer is not None else "IMPOSSIBLE"))

if __name__ == "__main__":
    sys.exit(main())
