#!/usr/bin/env python

import sys

sys.stdin = file("b-input")
sys.stdout = file("b-output", "w")

input_count = int(raw_input())
for instance in range(input_count):
    dimensions = raw_input().split()
    rows, cols = int(dimensions[0]), int(dimensions[1])

    garden = [[0] * cols for row in range(rows)]
    for r in range(rows):
        row = raw_input().split()
        for c, col in enumerate(row):
            garden[r][c] = int(col)

    row_max = []
    col_max = []

    # compute row max for each row
    for row in garden:
        row_max.append(max(row))

    for c in range(cols):
        col = [row[c] for row in garden]
        col_max.append(max(col))

    can_do = "YES"
    for r in range(rows):
        for c in range(cols):
            if row_max[r] != garden[r][c] and col_max[c] != garden[r][c]:
                can_do = "NO"

    print "Case #%i: %s" % (instance + 1, can_do)
