#!/usr/bin/env python

import math

def run_one(X, R, C):
    if R * C % X != 0:
        return 'RICHARD'

    if X == 3:
        # n x 3
        if R == 1 or C == 1:
            return 'RICHARD'
    elif X == 4:
        # 2 x 2 or n x 4
        if R == 1 or C == 1 or R == 2 or C == 2:
            return 'RICHARD'

    return 'GABRIEL'


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        X, R, C = (int(i) for i in lines.popleft().split(' '))

        result = run_one(X, R, C)

        output.append('Case #{0}: {1}'.format(t + 1, result))

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque(file.readlines())
        output = run(lines)
        print os.linesep.join(output)
