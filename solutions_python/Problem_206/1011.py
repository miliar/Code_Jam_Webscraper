#! /usr/bin/env python

import sys


def solve(distance, horses):
    # get the last arriving horse
    max_time = 0
    for start, speed in horses:
        remaining_distance = distance - start
        time = remaining_distance / speed
        max_time = max(max_time, time)

    return distance / max_time


def progress(s):
    print("%-80s\r" % s, file=sys.stderr, end='')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
    else:
        inputfile = 'input.test'
    with open(inputfile) as f:
        cases = int(f.readline())
        for i in range(cases):
            progress(i + 1)
            D, N = map(int, f.readline().strip().split())
            print('Case #%d: %s' % (
                i+1,
                solve(
                    distance=D,
                    horses=[
                        map(int, f.readline().strip().split())
                        for _ in range(N)
                    ]
                )
            ))
