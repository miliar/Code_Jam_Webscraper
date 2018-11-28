#!/usr/bin/python

import sys

def is_tidy(s):
    c = 0
    for i in range(len(s)):
        digit = int(s[i])
        if c > digit:
            return False
        else:
            c = digit
    return True

lines = open(sys.argv[1], 'r').readlines()
case = 0
for line in lines[1:]:
    num = long(line.strip())
    res = ""
    for i in xrange(num, 0, -1):
        n = str(i)
        if len(n) > 10:
            res = "9" * (len(n)-1)
            break
        elif is_tidy(n):
            res = n
            break
    case += 1
    print "Case #%d: %s" % (case, res)
