#!/usr/bin/env python

import sys
import re

n = int(sys.stdin.readline().strip())

what = "welcome to code jam"

def find(txt, what):
#    print txt, '/', what
    if len(what) == 0:
#        print '*'
        return 1
    pos = 0
    cnt = 0
    while True:
        pos = txt.find(what[0], pos)
#        print pos
        if pos == -1:
            break
        found = find(txt[pos+1:], what[1:])
#        print "found", found
        if not found:
            break
        cnt += found
        if cnt >= 1000:
            cnt -= 1000
        pos += 1
    return cnt
    

for i in xrange(n):
#    print i
    txt = sys.stdin.readline().strip()
    cnt = find(txt, what)


    print "Case #%d: %04d" % (i+1, cnt)








