#!/usr/bin/python
import sys
from copy import copy


def playKen(naomiTell, ken):
    # Return smallest item in ken which is greater than naomiTell
    # If there is no such item, return the smallest item
    # Assumes that ken is ordered in descending order
    for i, x in enumerate(ken):
        index = len(ken) - (i + 1)
        if ken[index] > naomiTell:
            return ken.pop(index)
    return ken.pop()


def playNaomi(naomi, ken, deceive):
    if not deceive:
        return naomi.pop(0)
    smallest = naomi[len(naomi) - 1]
    if all(k > smallest for k in ken):
        naomi.pop()
        return ken[0] - 0.0000001
    for i in range(len(naomi)):
        index = len(naomi) - (i + 1)
        if naomi[index] > ken[len(ken) - 1]:
            naomi.pop(index)
            return ken[0] + 0.0000001
    naomi.pop()
    return ken[0] - 0.0000001


def play(naomiCop, kenCop, deceive=False):
    naomi = sorted(copy(naomiCop), reverse=True)
    ken = sorted(copy(kenCop), reverse=True)
    opt = 0
    while len(ken):
        naomiTell = playNaomi(naomi, ken, deceive)
        kenTell = playKen(naomiTell, ken)
        if naomiTell > kenTell:
            opt += 1
    return opt


def solve(naomi, ken):
    y = play(naomi, ken, deceive=True)
    z = play(naomi, ken)
    return "%d %d" % (y, z)


if __name__ == '__main__':
    lines = map(lambda line: line.strip(), sys.stdin.readlines())
    i = 1
    case = 1
    while i < len(lines):
        nu = int(lines[i])
        naomi = map(float, lines[i + 1].split())
        ken = map(float, lines[i + 2].split())
        sol = solve(naomi, ken)
        print "Case #%s: %s" % (case, sol)
        case += 1
        i += 3
