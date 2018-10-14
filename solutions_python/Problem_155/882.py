#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(smax, sstr):
    friends = 0
    up = 0
    for k, digit in enumerate(sstr):
        digit = int(digit)
        if digit > 0 and up < k:
            new_friends = k - up
            up += new_friends
            friends += new_friends
        up += digit
    return friends


if __name__ == "__main__":
    testcases = int(raw_input())

    for caseNr in range(1, testcases+1):
        smax, sstr = raw_input().split(" ")
        print("Case #%i: %s" % (caseNr, solve(smax, sstr)))
