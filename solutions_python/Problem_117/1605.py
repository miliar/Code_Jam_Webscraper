#!/usr/bin/env python

import fileinput

def is_valid(lawn, x, y, level):
    check1 = True
    for i in range(0, len(lawn)):
        if lawn[i][y] is not level:
            check1 = False
    check2 = True
    for j in range(0, len(lawn[0])):
        if lawn[x][j] is not level:
            check2 = False
    return check1 or check2

def backtrack(lawn):
    current = max(max(lawn))
    prev = current
    for i in range(0, len(lawn)):
        for j in range(0, len(lawn[0])):
            if lawn[i][j] < current:
                prev = current
                current = lawn[i][j]

    # check validity
    for i in range(0, len(lawn)):
        for j in range(0, len(lawn[0])):
            if lawn[i][j] is current:
                if not is_valid(lawn, i, j, current):
                    return False

    # fill current with prev
    for i in range(0, len(lawn)):
        for j in range(0, len(lawn[0])):
            if lawn[i][j] is current:
                lawn[i][j] = prev
    return True

def is_complete(lawn):
    return min(min(lawn)) is max(max(lawn))


def solve(lawn, case):
    while True:
        good = backtrack(lawn)
        if not good:
            result = "NO"
            break;
        elif is_complete(lawn):
            result = "YES"
            break;
    print "Case #%d: %s" % (case, result)

cases = 0
lawn = []
current_case = 0
current_line = 0
new_lawn = False
rows = 0
cols = 0
for line in fileinput.input():
    line = line.strip()
    current_line += 1
    if current_line is 1:
        new_lawn = True
        continue
    if new_lawn:
        dim = line.split(" ")
        assert len(dim) is 2
        rows = int(dim[0])
        cols = int(dim[1])
        new_lawn = False
        continue
    row = line.split(" ")
    assert len(row) is cols
    row_int = []
    for i in row:
        row_int.append(int(i))
    lawn.append(row_int)
    if len(lawn) is rows:
        current_case += 1
        solve(lawn, current_case)
        lawn = []
        new_lawn = True

