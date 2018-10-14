#!/usr/bin/env python
from itertools import count
import sys

if len(sys.argv) != 2:
    print 'Usage: python shit.py <input file>'

with open(sys.argv[1]) as f:
    text = f.readlines()
    numTestcases = text[0]
    testcases = map(lambda x: x.split(), text[1:])

for (sdata, tc) in zip(map(lambda x: x.split()[1], text[1:]),count(1,1)):
    index = 0 ; total = 0
    for index in range(len(sdata)):
        total = total + int(sdata[index]) + max(0, index-total)
    print 'Case #' + str(tc) + ': ' + str(total - sum(int(c) for c in sdata))
