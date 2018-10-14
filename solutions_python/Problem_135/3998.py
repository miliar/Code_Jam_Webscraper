#!/usr/bin/env python
# -*- coding: utf-8 -*

"""GCJ 2014 Qualification Round: Problem A"""


def solve(A, B, tabA, tabB):
    out = 0
    tot = tabA[A-1] + tabB[B-1]

    for k in tot:
        if tot.count(k) > 1 and k != out:
            if out == 0:
                out = k
            else:
                out = -1  # bad
                break


    if out == -1:
        out = "Bad magician!"
    elif out == 0:
        out = "Volunteer cheated!"

    return out


if __name__ == "__main__":
    T = int(input())  # nb of test cases

    for x in range(T):
        A = int(input())
        tabA = [map(int, raw_input().split()) for i in xrange(4)]
        B = int(input())
        tabB = [map(int, raw_input().split()) for i in xrange(4)]

        y = solve(A, B, tabA, tabB)
        print("Case #%d: %s" % (x+1, y))
