#!/usr/bin/env python

def run_one(N, M, lawn):
    cut_n = [max(lawn[n]) for n in range(N)]
    cut_m = [max(lawn[n][m] for n in range(N)) for m in range(M)]

    for n in range(N):
        for m in range(M):
            if lawn[n][m] < cut_n[n] and lawn[n][m] < cut_m[m]:
                return 'NO'

    return 'YES'


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Size of rectangular lawn
        N, M = [int(x) for x in lines.popleft().split()]

        # Desired height grass in lawn
        lawn = [[int(height) for height in lines.popleft().split()] for row in range(N)]

        result = run_one(N, M, lawn)

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
