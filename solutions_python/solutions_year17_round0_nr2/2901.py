#!/usr/bin/env python

import sys

def tidy(num):
    num = list(num)
    c   = num[0]
    idx = 1
    while idx < len(num) and c <= num[idx]:
        c = num[idx]
        idx += 1

    if idx < len(num):
        idx -= 1

        while idx >= 0 and c == num[idx]:
            idx -= 1

        idx += 1

        num[idx] = str(int(num[idx]) - 1)

        idx += 1

        while idx < len(num):
            num[idx] = '9'
            idx += 1

    if num[0] == '0':
        num.pop(0)

    return "".join(num)

num = sys.stdin.readline()

for x in range(1, int(num) + 1):
    num = sys.stdin.readline().splitlines()[0]
    print "Case #" + str(x) + ": " + tidy(num)
