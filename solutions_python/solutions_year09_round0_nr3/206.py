#!/usr/bin/python
"Google Qualification - C"

import re

target = 'welcome to code jam'

cases = int(raw_input())

def subs(t, s):
    n = 0
    if not t:
        return 0
    c = t[0]
    for i in range(0, len(s)):
        if s[i] == c:
            if len(t) == 1:
                n += 1
            elif i < len(s):
                n += subs(t[1:], s[i+1:])
    return n

for case in range(1, cases + 1):
    line = raw_input().strip()
    n = subs(target, line)
    np = '%04d' % n
    #print np

    print 'Case #%d: %s' % (case, np[-4:])
