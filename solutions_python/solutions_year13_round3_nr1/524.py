#!/usr/bin/env python
import re
import itertools

inp = open("A-small-attempt0.in")
lines = inp.readlines()

i = 1
for line in lines[1:]:
    (name, ns) = line.strip().split(" ")
    n = int(ns)
    j = 0
    pat = re.compile("([^aeiou]{%d})" % n)
    for e in itertools.combinations(range(len(name) + 1), 2):
        newname = name[e[0]:e[1]]
        if re.search(pat, newname):
            j += 1
    print "Case #%d: %d" % (i, j)
    i += 1

