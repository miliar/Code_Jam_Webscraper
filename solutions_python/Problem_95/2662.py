#!/usr/bin/env python
import sys

l2 = """qz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"""
l1 = """zq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"""

codebook = dict()
for i, char in enumerate(l2):
    codebook[char] = l1[i]

if len(sys.argv) > 1:
    f = file(sys.argv[1])
else:
    f = file('1sample.txt')

numlines = int(f.readline())
case = 1
for line in f:
    newline = ""
    for i, char in enumerate(line):
        if char == "\n": continue
        newline += codebook[char]
    print "Case #"+str(case)+": ", newline
    case += 1
