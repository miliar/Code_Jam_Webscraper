#!/usr/bin/env python
#coding:utf-8
#py2

def check(s):
    if len(s) > 1 and s[0] == '0':
        return False
    return list(s) == sorted(s)

T = int(raw_input().strip()) #1 100
for cas in xrange(1, T + 1):
    s = raw_input().strip() #1 1e18
    n = len(s) #n >= 1 
    res = -1
    if check(s):
        res = int(s)

    #the lowest high bits such that value - 1 >= prev or > prev
    #at least one high bits decrease, if s is not tidy. 
    #then focus only on the highest one because the right should be 9s.

    for h in xrange(n):
        t = s[:h] + chr(ord(s[h]) - 1) + '9'*(n - h - 1)
        if t[0] == '0':
            #h = 0, 1 => 0. s[1] >= (0 + 1)
            t = t[1:]
        if t and check(t):
            #ignore empty string for single digit 1 since 1 is sorted already
            res = max(res, int(t))
    print "Case #%d: %s" % (cas, res)
