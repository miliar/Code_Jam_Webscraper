#!/usr/bin/env python
import sys

cases = []
with open(sys.argv[1]) as f:
    for l in f:
        cases.append(l.strip().split(" "))
cases.pop(0)

caseno = 1
for max_s, peeps in cases:
    max_s = int(max_s)
    audience = [int(p) for p in peeps]

    friends = 0
    s = 0
    count = 0
    while s < max_s:
        count += audience[s]
        if count <= s:
            friends += 1
            count += 1
        s += 1

    print "Case #%s: %s" % (caseno, friends)
    caseno += 1
