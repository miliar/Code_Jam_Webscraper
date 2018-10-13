#!/usr/bin/python

import heapq

def stall_one(n):
    m = n - 1
    LS = m / 2
    RS = (m + 1) / 2
    return (LS, RS)

def stall_next(h):
    """modifies heap in place, returns LS/RS"""
    space = -heapq.heappop(h)
    pair = stall_one(space)
    LS = pair[0]
    RS = pair[1]
    if LS > 0:
        heapq.heappush(h, -LS)
    if RS > 0:
        heapq.heappush(h, -RS)
    return (LS, RS)

def stall_space(n, k):
    h = [-n]
    heapq.heapify(h)
    for i in xrange(k):
        pair = stall_next(h)
    return pair

num_lines = int(raw_input())
for i in xrange(num_lines):
    pair = raw_input().split()
    N = int(pair[0]) # num stalls
    K = int(pair[1]) # num people
    LS, RS = stall_space(N, K)
    print "Case #%d: %d %d" % (i+1, max(LS, RS), min(LS, RS))
