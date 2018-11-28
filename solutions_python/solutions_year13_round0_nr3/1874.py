#!/usr/bin/python

import math
inputf = open("C-small-attempt0.in")
lines = inputf.readlines()
num = int(lines[0])
j = 1
for line in lines[1:]:
    line = line.strip()
    a, b = map(lambda x: int(x), line.split(" "))
    r = 0
    for n in range(a, b + 1):
        nr = int(str(n)[::-1])
        ns = math.sqrt(n)
        nsi = int(ns)
        if n == nr and math.ceil(ns) == math.floor(ns) and str(nsi) == str(nsi)[::-1]:
            r = r + 1
    print "Case #" + str(j) + ": " + str(r)
    j = j + 1

