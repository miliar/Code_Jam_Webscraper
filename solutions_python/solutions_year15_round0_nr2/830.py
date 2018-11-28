#!/usr/bin/env python

import math

def run_one(pancake_counts):
    max_pancakes = max(pancake_counts)

    min_minutes = max_pancakes

    for eating_minutes in range(2, max_pancakes):
        special_minutes = 0

        for count in pancake_counts:
            special_minutes += int(math.ceil(1.0 * count / eating_minutes)) - 1

        min_minutes = min(min_minutes, eating_minutes + special_minutes)

    return min_minutes


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        D = int(lines.popleft())
        pancake_counts = [int(s) for s in lines.popleft().split(' ')]

        result = run_one(pancake_counts)

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
