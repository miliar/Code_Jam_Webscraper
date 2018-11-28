#!/usr/bin/env python2.7

import sys


def judge_case(ans1, cards1, ans2, cards2):
    candidates = set(cards1[ans1 - 1])
    candidates &= set(cards2[ans2 - 1])
    if len(candidates) > 1:
        return 'Bad magician!'
    elif len(candidates) == 0:
        return 'Volunteer cheated!'
    else:
        return str(candidates.pop())


def read_case(f):
    ans1 = int(f.readline())
    cards1 = [[int(x) for x in f.readline().split()] for i in xrange(4)]
    ans2 = int(f.readline())
    cards2 = [[int(x) for x in f.readline().split()] for i in xrange(4)]

    return (ans1, cards1, ans2, cards2)

filename = sys.argv[1]

with open(filename) as f:
    n_cases = int(f.readline())
    for i in xrange(n_cases):
        case = read_case(f)
        print "Case #{}: {}".format(i + 1, judge_case(*case))
