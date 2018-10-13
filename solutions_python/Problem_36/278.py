#!/usr/bin/python

import sys

NEEDLE = 'welcome to code jam'

def rstr(in_file=sys.stdin):
    return in_file.readline().strip()

def rint(in_file=sys.stdin):
    return int(rstr(in_file))

def counter(haystack, needle):
    if len(needle) == 0:
        return 1
    sum = 0
    pos = haystack.find(needle[0])
    if pos >= 0:
        sum += counter(haystack[pos+1:], needle[1:])
        sum %= 1000
        sum += counter(haystack[pos+1:], needle)
        sum %= 1000
    return sum
    
def run():
    cases = rint()
    for c in range(cases):
        haystack = rstr()
        n = counter(haystack, NEEDLE)
        print 'Case #%s: %s' % (c+1, str(int(n)).zfill(4))

run()