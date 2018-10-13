#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(a, b):

    intersection = set(a) & set(b)
    N = len(intersection)

    if N == 0:
        return "Volunteer cheated!"
    elif N > 1:
        return "Bad magician!"
    else:
        return intersection.pop()

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        a = int(raw_input()) - 1
        grid = []

        for row in xrange(1, 5):
            grid.append(raw_input().split(" "))

        b = int(raw_input()) - 1
        grid2 = []

        for row in xrange(1, 5):
            grid2.append(raw_input().split(" "))

        print("Case #%i: %s" % (caseNr, solve(grid[a], grid2[b])))