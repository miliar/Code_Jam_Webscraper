#!/usr/bin/env python

import sys


def min_flips(layout, flipper_width):
    flips = 0
    while len(layout) > flipper_width:
        if layout[-1]:
            layout.pop()
        else:
            flips += 1
            for i in xrange(len(layout)-flipper_width, len(layout)):
                layout[i] = not layout[i]
    if len(filter(lambda x: x, layout)) == len(layout):
        return flips
    elif len(filter(lambda x: not x, layout)) == len(layout):
        return flips + 1
    else:
        return -1


def solve_from_input():
    case_count = int(sys.stdin.readline().strip())
    for i in xrange(1, case_count + 1):
        rawlayout, width = sys.stdin.readline().strip().split()
        width = int(width)
        layout = []
        for x in rawlayout:
            layout.append(True if x == '+' else False)
        solution = min_flips(layout, width)
        sys.stdout.write('Case #{}: '.format(i))
        if solution == -1:
            sys.stdout.write('IMPOSSIBLE\n')
        else:
            sys.stdout.write('{}\n'.format(solution))


if __name__ == '__main__':
    solve_from_input()
