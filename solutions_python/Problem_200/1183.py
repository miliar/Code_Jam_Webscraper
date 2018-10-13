#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline().strip())

for case in range(cases):
    num = [int(x) for x in sys.stdin.readline().strip()]

    pos = len(num) - 1
    while pos > 0:
        if num[pos] < num[pos-1]:
            num[pos:] = [9]*(len(num)-pos)
            num[pos-1] -= 1
        pos -= 1

    sys.stdout.write("Case #%d: %d\n" % (
        case+1,
        int("".join([str(x) for x in num]))))
