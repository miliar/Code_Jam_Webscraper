#!/usr/bin/env python
import fileinput
def getlines():
    inp = fileinput.input()
    for line in inp:
        yield map(int, line.rstrip().split())

getline = getlines()
cases = getline.next()[0]

def check_possible(rows, x, y):
    for i in range(x):
        for j in range(y):
            val = rows[i][j]
            higher = 0
            for sub_i in range(x):
                if rows[sub_i][j] > val:
                    higher += 1
                    break
            for sub_j in range(y):
                if rows[i][sub_j] > val:
                    higher += 1
                    break
            if higher == 2:
                return False
    return True

for case in range(cases):
    x, y = getline.next()
    rows = [getline.next() for i in range(x)]
    result = None
    for row in rows:
        for j in row:
            if j > 100:
                result = "NO"
    if not result:
        result = "YES" if check_possible(rows, x, y) else "NO"

    print("Case #%d: %s" % (case + 1, result))
