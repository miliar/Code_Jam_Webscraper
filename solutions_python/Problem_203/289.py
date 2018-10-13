#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fill_line(line):
    letters = list(line)
    started = False
    lastchar = '='
    for i in range(len(letters)):
        if letters[i] == '?':
            if not started:
                pass
            else:
                letters[i] = lastchar
        else:
            lastchar = letters[i]
            if not started:
                for j in range(i):
                    letters[j] = lastchar
                started = True
    return ''.join(letters)


T = int(input())  # number of test cases
for t in range(T):
    R, C = [int(v) for v in input().split()]  # rows and columns
    grid = list()
    for r in range(R):
        grid.append(input().strip())

    empty = list()
    occup = list()
    for r in range(R):
        allint = True
        for c in range(C):
            if grid[r][c] != '?':
                allint = False
        if allint:
            empty.append(r)
        else:
            occup.append(r)
    # fill lines that contain at least an initial
    for r in occup:
        grid[r] = fill_line(grid[r])
    # copy lines that
    for r in empty:
        # closest line
        closest = -1
        dist = 1e3
        for rc in occup:
            dis = abs(rc - r)
            if dis < dist:
                dist = dis
                closest = rc
        grid[r] = grid[closest]

    print("Case #{:d}:".format(t + 1))
    for line in grid:
        print(line)
