#!/usr/bin/env python

import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    phrase = "welcome to code jam"

    perms = [0] * len(phrase)

    word = sys.stdin.readline().strip()
    for letter in word:
        for index in range(len(phrase)):
            if letter == phrase[index]:
                if index > 0:
                    perms[index] += perms[index-1]
                else:
                    perms[0] += 1
                perms[index] -= (perms[index] / 10000) * 10000
        

    if (perms[-1] >= 1000):
        print "Case #%d: %d" % (i+1,perms[-1])
    elif perms[-1] >= 100:
        print "Case #%d: 0%d" % (i+1,perms[-1])
    elif perms[-1] >= 10:
        print "Case #%d: 00%d" % (i+1,perms[-1])
    elif perms[-1] >= 0:
        print "Case #%d: 000%d" % (i+1, perms[-1])
