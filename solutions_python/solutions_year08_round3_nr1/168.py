#!/usr/local/bin/python
from math import ceil
for case in range(input()):
    p, k, l = map(int, raw_input().split())
    k = float(k)
    letters = sorted(map(int, raw_input().split()))[::-1]
    presses = 0
    for i in range(len(letters)):
        presses += letters[i] * int(ceil((i+1)/k))
    print "Case #%d: %d" % (case+1, presses)
        
