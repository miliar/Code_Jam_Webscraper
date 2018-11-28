#!/usr/bin/env python

def solve(discs, capacity):
    count = 0
    i = 0
    j = len(discs) - 1
    while i < j:
        if discs[i] + discs[j] <= capacity:
            i += 1
            j -= 1
        else:
            j -= 1
        count += 1
    if i == j:
        count += 1
    print count

for case in xrange(int(raw_input())):
    print "Case #%d:" % (case+1),
    num_discs, capacity = map(int, raw_input().split())
    discs = map(int, (raw_input().split()))
    solve(sorted(discs), capacity)
