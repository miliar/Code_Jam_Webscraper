#!/usr/bin/env python
# -*- coding: utf-8 -*

"""GCJ 2015 Qualification Round: Problem A."""


def solve(s):
    out = 0
    people = 0

    for si, str_k in enumerate(s):
        k = int(str_k)
        if people < si:
            diff = si - people
            people += diff
            out += diff

        people += k

    return out


if __name__ == "__main__":
    T = int(input())  # nb of test cases

    for x in range(T):
        smax, s = input().split()

        y = solve(s)
        print("Case #%d: %s" % (x+1, y))
