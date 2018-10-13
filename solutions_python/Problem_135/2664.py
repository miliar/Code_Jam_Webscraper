#!/usr/bin/env python

T = int(raw_input())

def read_matrix():
    return [[int(x) for x in line.strip().split()] for line in [raw_input() for i in xrange(4)]]

for case in xrange(1, T+1):
    r1 = int(raw_input())
    m1 = read_matrix()
    r2 = int(raw_input())
    m2 = read_matrix()

    results = set(m1[r1-1]) & set(m2[r2-1])
    if len(results) == 1:
        answer = str(next(iter(results)))
    elif not results:
        answer = "Volunteer cheated!"
    else:
        answer = "Bad magician!"
    print "Case #%d: %s" % (case, answer)
