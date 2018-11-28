#!/usr/bin/python

import math

def ispali(n):
    s = str(n)
    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True

with open("input.txt") as f:
    nsquares = int(f.readline())
    for n in range(nsquares):
        lims = f.readline().split(' ')
        a = int(lims[0])
        b = int(lims[1])
        palis = 0
        for i in range(a, b+1):
            if ispali(i):
                root = int(math.sqrt(i))
                if root * root == i:
                    if ispali(root):
                        palis += 1
        print 'Case #{}:'.format(n+1), palis
