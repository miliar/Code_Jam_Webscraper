#!/usr/bin/env python

from collections import deque
import sys

def solved(rows):
    for i, j in enumerate(rows):
        if j > i:
            return False
    return True

def solve(rows):
    if solved(rows):
        return 0

    seen = set()
    seen.add('|'.join(map(str, rows)))
    q = deque([(rows, 0)])
    while q:
        r, m = q.popleft()
        m += 1
        for i in range(len(rows)-1):
            p = r[:i] + [r[i+1],r[i]] + r[i+2:]
            ps = '|'.join(map(str, p))
            if ps in seen:
                continue
            if solved(p):
                return m
            seen.add(ps)
            q.append((p, m))
    

T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    rows = [raw_input().rfind('1') for n in range(N)]
    print "Case #%d: %d" % (t+1, solve(rows))
    sys.stdout.flush()
