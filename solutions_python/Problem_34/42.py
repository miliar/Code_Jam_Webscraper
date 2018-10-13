#!/usr/bin/env python

def match(pattern, words):
    sets = []
    inparens = False
    start = -1
    for i in range(len(pattern)):
        if pattern[i] == '(':
            inparens = True
            start = i+1
        elif pattern[i] == ')':
            sets.append(pattern[start:i])
            inparens = False
        elif not inparens:
            sets.append(pattern[i])
        else:
            pass

    count = 0
    for word in words:
        for i in range(len(word)):
            if word[i] not in sets[i]:
                break
        else:
            count += 1
    return count
        

import sys
l,d,n = map(int, sys.stdin.readline().split())

words = [ sys.stdin.readline().strip() for i in range(d) ]

c = 0
for line in sys.stdin:
    c += 1
    print "Case #%d:" % c, match(line.strip(), words)
