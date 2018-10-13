#!/usr/bin/env python

def run_one(s_counts):
    invited = 0
    clapping = 0

    for s, count in enumerate(s_counts):
        invited = max(invited, s - clapping)
        clapping += count

    return invited


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        s_max, s_list = lines.popleft().rstrip('\r\n').split(' ')
        s_counts = [int(s) for s in s_list]

        result = run_one(s_counts)

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
