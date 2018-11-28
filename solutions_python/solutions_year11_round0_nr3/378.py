#!/usr/bin/python
import string

def solve(s):
    r = map(string.atoi, s.split())
    if reduce(lambda x, y: x^y, r, 0):
        return -1
    else:
        return sum(r) - min(r)

f = open("input.txt", "r")
lines = [x for x in f]
f.close()

t = string.atoi(lines[0])
for i in range(1, t + 1):
    ans = solve(lines[i*2])
    if ans == -1:
        print "Case #%d: NO" % i
    else:
        print "Case #%d: %d" % (i, ans)

