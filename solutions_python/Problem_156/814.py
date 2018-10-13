#!/usr/bin/env python

import sys


def token_stream():
    for s in sys.stdin:
        for x in s.rstrip().split():
            yield x

def get_min_amount(memo, p, index, prev_minutes):
    if index == len(p):
        return prev_minutes
    if (index, prev_minutes) in memo:
        return memo[index, prev_minutes]
    cur = p[index]
    res = 1000000000
    for parts in xrange(1, cur + 1):
        worst = (cur + parts - 1) / parts
        res = min(res, parts - 1 + get_min_amount(memo, p, index + 1, max(prev_minutes, worst)))
    memo[index, prev_minutes] = res
    return res


def solve(p):
    return get_min_amount({}, p, 0, 0)

inp = token_stream()

T = int(next(inp))
for case in xrange(T):
    n = int(next(inp))
    p = []
    for _ in xrange(n):
        p.append(int(next(inp)))

    print "Case #{}: {}".format(case + 1, solve(p))

