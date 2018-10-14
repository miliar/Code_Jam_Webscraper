#!/usr/bin/env python

import sys

def iterate_input():
    t = int(sys.stdin.readline())
    for i in range(t):
        line = sys.stdin.readline().split(' ')
        a, b = map(int, line[0:2])
        yield i+1, a, b

def recycle(n, b):
    mlist = []
    nstr = str(n)
    for size in range(1, len(nstr)):
        m = int(nstr[len(nstr)-size:]+nstr[:len(nstr)-size])
        if n < m <= b:
            mlist.append(m)
    return set(mlist)
        
ranges_counts = []
for case_no, a, b in iterate_input():
    ranges_counts.append([a, b, 0])
min_a = min(a for a, b, c in ranges_counts)
max_b = max(b for a, b, c in ranges_counts)

for n in range(min_a, max_b):
    mlist = recycle(n, max_b)
    for m in mlist:
        for range_count in ranges_counts:
            a, b = range_count[0:2]
            if a <= n < m <= b:
                range_count[2] += 1

for i in range(len(ranges_counts)):
    count = ranges_counts[i][2]
    print "Case #%d: %d" % (i+1, count)

