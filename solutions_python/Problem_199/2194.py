#!/usr/bin/python
# coding=utf8

import sys

happyStr = "+"
blankStr = "-"

nbCases = 0

index = -1
for line in sys.stdin:
    index += 1
    if index == 0:
        nbCases = int(line)
        continue
    
    s, k = line.split()
    flip = 0
    for i in xrange(len(s)):
        if s[i] == blankStr:
            flip += 1
            tmp = ""
            for y in xrange(int(k)):
                tmp += happyStr if s[i + y] == blankStr else blankStr
            s = s[:i] + tmp + s[i + int(k):]
        
        if i == (len(s) -int(k)):
            if s.find(blankStr) == -1:
                print "case #" + str(index) + ": " + str(flip)
            else:
                print "case #" + str(index) + ": IMPOSSIBLE"
            break