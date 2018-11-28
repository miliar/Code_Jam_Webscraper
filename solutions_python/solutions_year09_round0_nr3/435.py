#!/usr/bin/python

import sys

lines = sys.stdin.readlines()

def countSubsequences(rest, seq):
    if seq == '': return 1
    
    total = 0
    for i in range(0, len(rest)):
        if rest[i] == seq[0]:
            total += countSubsequences(rest[i+1:], seq[1:])
    return total % 1000

cases = int(lines[0])
search = 'welcome to code jam'
index = 1
for test in lines[1:]:
    print 'Case #' + str(index) + ': %04d' % countSubsequences(test, search)
    index += 1
