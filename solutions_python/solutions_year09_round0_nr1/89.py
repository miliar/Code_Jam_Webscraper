#!/usr/bin/env python

import sys, re

dictionary = []

def chk(message):
    reg = re.compile("^" + message.replace("(","[").replace(")","]") + "$")
    cnt = 0
    for d in dictionary:
        if reg.match(d):
            cnt += 1
    return cnt

file=sys.stdin
l,d,n = map(int, file.readline().strip().split())
for x in range(d):
    dictionary.append( file.readline().strip() )
    if len(dictionary[-1]) != l:
	raise Exception("word '%s' isn't %d letters long" % (dictionary[-1], l))
for case_n in range(n):
    message = file.readline().strip()
    print "Case #%d: %d" % (case_n+1, chk(message))

