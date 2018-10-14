#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

data = []
for line in file("A-large.in"):
    data.append(line.strip())

L, D, N = map(int, data[0].split())


words = data[1:1+D]
tests = data[1+D:1+D+N]

tests_re = []

for i, test in enumerate(tests):
    tests_re.append(re.compile(test.replace("(", "[").replace(")", "]")))

for i, test in enumerate(tests_re):
    count = 0
    for word in words:
        if test.match(word):
            count += 1
    print "Case #%d: %d" % (i+1, count)
