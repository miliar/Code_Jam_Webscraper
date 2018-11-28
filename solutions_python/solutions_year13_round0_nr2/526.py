#!/usr/bin/python
import sys

# Lawnmower

i = 0
lines = [l.rstrip() for l in sys.stdin.readlines()]
for x in xrange(int(lines[i])):
    n, m = map(int, lines[i+1].split())
    lawn = [map(int, line.split()) for line in lines[i+2:i+2+n]]
    flat = [c for r in lawn for c in r]
    for l in xrange(min(flat), max(flat)+1):
        filtered = filter(lambda r: r.count(l) != len(r), lawn)
        lawn = filter(lambda r: r.count(l) != len(r), zip(*filtered))
    print("Case #%u: %s" % (x + 1, "NO" if len(lawn) else "YES"))
    i += n + 1
