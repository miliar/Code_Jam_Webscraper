#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def eat(pancakess):
    if pancakess[0] < 3:
        return pancakess[0]
    top = pancakess[0]
    # print pancakess
# route 1
    pancakes1 = list(pancakess)
    tmp = 3 if top == 9 else top / 2
    pancakes1[0] = tmp
    pancakes1.append(top - tmp)
    pancakes1 = sorted(pancakes1, reverse=True)

# route 2
    pancakes2 = [x - 1 for x in pancakess]

    return (1 + min(eat(pancakes1), eat(pancakes2)))

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        diners = raw_input()
        pancakes = raw_input()
        pancakes = sorted([int(x) for x in pancakes.split()], reverse=True)
        print("Case #%i: %s" % (caseNr, eat(pancakes)))
