#!/usr/bin/env py3k
"""GCJ 2009, Round 1C, Problem A solver."""
from sys import stdin
from baseconvert import baseconvert
from itertools import permutations
from re import sub

lines = stdin.readlines()
nocases = lines.pop(0)
caseno = 1

for line in lines:
    alpha = ''
    line = line.strip()
    for char in line:
        if not char in alpha:
            alpha += char
    lowest = None
    for tup in permutations(alpha):
        myalpha = ''.join(tup)
        myline = ''
        if myalpha.index(line[0]) == 0:
            if len(myalpha) > 1:
                continue
            else:
                myalpha = ' ' + myalpha
        for char in line:
            myline += str(myalpha.index(char))
        i = int(sorted(str(myline))[-1]) + 1
        if i == 1:
            i = 2
        l = int(myline, i)
        if lowest is None:
            lowest = l
            continue
        if l < lowest:
            lowest = l
    if lowest is None:
        print('line: %s, alpha: %s' % (line, alpha))
    print('Case #%s: %s' % (caseno, lowest))
    caseno += 1