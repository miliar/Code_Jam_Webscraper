#! /usr/bin/python2.7

from Queue import PriorityQueue

def add_to(counts, v, count):
    if v not in counts:
        counts[v] = count
    else:
        counts[v] += count

def solve(n, k):
    q = PriorityQueue()
    counts = {n: 1}
    q.put(-n)
    while k > 0:
        v = -q.get()
        if v not in counts:
            continue
        count = counts[v]
        del counts[v]
        k -= count
        if k <= 0:
            return v
        if v % 2 == 1:
            q.put(-(v / 2))
            add_to(counts, v / 2, count * 2)
        else:
            q.put(-(v / 2))
            add_to(counts, v / 2, count)
            q.put(-((v / 2) - 1))
            add_to(counts, (v / 2) - 1, count)

import sys
f = sys.stdin
# f = open("q3_example.in")
T = int(f.readline())
for i in xrange(1, T + 1):
    N, K = map(int, f.readline().split())
    v = solve(N, K)
    if v % 2 == 0:
        v1, v2 = v / 2, (v / 2) - 1
    else:
        v1, v2 = v / 2, v / 2
    print "Case #%d: %d %d" % (i, v1, v2)