#!/usr/bin/env python

import sys


def check(test):
    c, f, x = float(test[0]), float(test[1]), float(test[2])
    cookies = 2
    time = 0.0
    while(True):
        time1 = time + x / cookies
        time2 = time + c / cookies + x / (cookies + f)
        if time2 < time1:
            time += c / cookies
            cookies += f
        else:
            return time1

    print(c, f, x)

testcases = sys.stdin.readline()


for testcase in range(0, int(testcases)):
    test = sys.stdin.readline().strip().split(" ")
    result = check(test)
    print("Case #{0}: {1}".format(testcase + 1, result))
