#!/usr/bin/env python

import os, sys

cdict = {' ':' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z':'q', 'q':'z'}

def solve (line):
    newline = ""
    for x in line:
        newline += cdict[x]
    return newline


fd = sys.stdin

line = fd.readline()
sets = int(line)+1

for case in range(1, sets):
    line = fd.readline().strip()
    nline = solve(line)
    print "Case #%s: %s" % (case, nline)

fd.close()
