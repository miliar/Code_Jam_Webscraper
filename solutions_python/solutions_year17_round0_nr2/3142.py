#!/usr/bin/env python2

import sys

def tidy(n):
    for i in xrange(len(n)-2, -1, -1):
        if n[i] > n[i+1]:
            n = list(str(int(''.join(n[:i+2]))-1)) + ['9'] * (len(n) - (i+2))
    return n

stdin = sys.stdin.readlines()
stdin.pop(0)
counter = 1
while len(stdin):
    n = list(stdin.pop(0).strip())
    m = tidy(n)
    while n != m:
        n = m
        m = tidy(n)
    print "Case #" + str(counter) + ": " + ''.join([str(j) for j in n])
    counter += 1
