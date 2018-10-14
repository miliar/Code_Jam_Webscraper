#!/usr/bin/env python
import sys
from itertools import dropwhile
import math

pairs = {}
sl = set()
fa = set()
def recycled(n, m):
    n, m = map(lambda x: "".join(dropwhile(lambda y: y == "0", list(str(x)))), [n, m])
    if len(n) != len(m):
        return False
    if pairs.has_key((n, m)):
        return pairs[(n,m)]
    for i in range(1, len(m)):
        if m[i:] + m[:i] == n:
            pairs[(n,m)] = True
            sl.add((int(n), int(m)))
            #print((n, m))
            return True
    return False

def slow(a, b):
    count = 0
    for n in range(a, b):
        for m in range(n + 1, b):
            if recycled(n, m):
                count += 1
    return count

def recycled_fast(n, b):
    s = str(n)
    out = []
    for i in range(1, len(s)):
        out.append(s[i:] + s[:i])
    out = map(int, out)
    out = filter(lambda x: int(math.log10(n)) == int(math.log10(x)), out)
    out = filter(lambda x: n < x <= b, out)
    for c in out:
        fa.add((n, c))
    return len(set(out))

def fast(a, b):
    count = 0
    for n in range(a, b):
        count += recycled_fast(n, b)
    return count

for case in range(1, int(sys.stdin.readline()) + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d" % (case, fast(a, b)))
