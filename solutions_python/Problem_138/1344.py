#! /usr/bin/env python -u
# coding=utf-8
from copy import deepcopy
import sys

__author__ = 'xl'


def play(l1, l2):
    if len(l1) == 0:
        return 0

    if min(l1) > max(l2):
        return len(l1)

    ret = 0

    while len(l1) > 0 and (min(l2) > min(l1) or max(l2) > max(l1)):
        l2.remove(max(l2))
        l1.remove(min(l1))

    if len(l1) > 0:
        ret += 1
        l2.remove(min(l2))
        l1.remove(min(l1))

    ret += play(l1, l2)
    return ret


def best_response(woods, q):
    responses = filter(lambda x: x > q, woods)
    if len(responses) > 0:
        return min(responses)
    else:
        return min(woods)


if __name__ == "__main__":
    fp = open("D.in")
    sys.stdout = open("D.out", "w")
    # fp = sys.stdin
    T = int(fp.readline())
    for t in range(T):
        n = int(fp.readline())
        p1 = p2 = 0

        woods1 = map(float, fp.readline().split())
        woods2 = map(float, fp.readline().split())
        woods1.sort()
        woods2.sort()

        # p1 = n-len(filter(lambda x: x < l2[0], l1))
        l1 = deepcopy(woods1)
        l2 = deepcopy(woods2)
        p1 = play(l1, l2)

        l2 = deepcopy(woods2)
        p2 = 0
        for val in woods1:
            res = best_response(l2, val)
            p2 += 0 if res > val else 1
            l2.remove(res)

        print "Case #%s: %d %d" % (t + 1, p1, p2)



