#!/usr/bin/env python

import sys


def check(test1, row1, test2, row2):
    rowa = test1[int(row1) - 1]
    rowb = test2[int(row2) - 1]
    setr = set(rowa) & set(rowb)
    if len(setr) == 0:
        return "Volunteer cheated!"
    if len(setr) > 1:
        return "Bad magician!"
    return setr.pop()

testcases = sys.stdin.readline()


for testcase in range(0, int(testcases)):
    row1 = sys.stdin.readline().strip()
    test1 = []
    for row in range(4):
        test1.append(sys.stdin.readline().strip().split(" "))
    row2 = sys.stdin.readline().strip()
    test2 = []
    for row in range(4):
        test2.append(sys.stdin.readline().strip().split(" "))
    result = check(test1, row1, test2, row2)
    print("Case #{0}: {1}".format(testcase + 1, result))
