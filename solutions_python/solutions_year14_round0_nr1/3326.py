#!/usr/bin/env python

T = int(raw_input())


def read_and_return_candidates(row):
    candidates = set()
    for r in xrange(1, 5):
        nums = map(int, raw_input().strip().split())
        if r == row:
            candidates = set(nums)
    return candidates


for t in xrange(1, T + 1):
    candidates = set()
    r1 = int(raw_input())
    c1 = read_and_return_candidates(r1)
    r2 = int(raw_input())
    c2 = read_and_return_candidates(r2)
    candidates = c1.intersection(c2)
    print 'Case #%d:' % t,
    if not candidates:
        print 'Volunteer cheated!'
    elif len(candidates) > 1:
        print 'Bad magician!'
    else:
        print candidates.pop()

