# GCJ 2014 Qualification, problem A, Jeremy Holman

import sys


T = int(sys.stdin.readline().strip())

for i in xrange(T):
    row_idx = int(sys.stdin.readline().strip())
    for j in xrange(4):
        raw_row = sys.stdin.readline().strip()
        if j+1 == row_idx:
            candidates = set(map(int, raw_row.split(' ')))
    row_idx = int(sys.stdin.readline().strip())
    for j in xrange(4):
        raw_row = sys.stdin.readline().strip()
        if j+1 == row_idx:
            new_candidates = set(map(int, raw_row.split(' ')))
            candidates.intersection_update(new_candidates)
    print "Case #%d:" % (i+1),
    if len(candidates) == 0:
        print "Volunteer cheated!"
    elif len(candidates) == 1:
        print list(candidates)[0]
    else:
        print "Bad magician!"




