#!/usr/bin/python

import sys

def flip(cake, i, k):
    if (i + k) > len(cake):
        return None
    for j in range(k):
        idx = i+j
        if cake[idx] == "+":
            cake[idx] = "-"
        else:
            cake[idx] = "+"

lines = open(sys.argv[1], 'r').readlines()
case = 0
for line in lines[1:]:
    items = line.strip().split(" ")
    cake = list(items[0])
    k = int(items[1])
    i = 0
    count = 0
    while cake != None and i < len(cake):
        #print cake, k
        if (cake[i] == '-'):
            flip(cake, i, k)
            count += 1
        #print cake
        i += 1
    res = str(count)
    for i in range(len(cake)):
        if cake[i] == '-':
            res = "IMPOSSIBLE"
    case += 1
    print "Case #%d: %s" % (case, res)
