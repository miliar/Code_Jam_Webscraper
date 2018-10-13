#!/usr/bin/env python

def f(arg):
    s = str(arg)
    for i in xrange(1, len(s)):
        if s[i] < s[i-1]:
            return False
    return True

def bf(n):
    while not f(n):
        n -= 1
    return n

def solve(s):
    m = -1
    for i in xrange(1, len(s)):
        if s[i] < s[i-1]:
            m = i-1
            break
    if m != -1:
        #return (s[:m] + str(int(s[m])-1) + "9"*(len(s)-m-1)).lstrip('0')
        ret = ''
        i = m-1
        while i >= 0:
            if s[i] != s[m]: break
            i -= 1    
        ret = s[:i+1]+str(int(s[m])-1) + "9"*(len(s)-i-2)
        return ret.lstrip('0')
    return s.lstrip('0')

n = input()
for i in xrange(n):
    m = raw_input()
    print "Case #%d: %s" % (i+1, solve(m))
