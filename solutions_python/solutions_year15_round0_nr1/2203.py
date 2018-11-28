#!/usr/bin/python

import sys

def ovation(str):
    count = 0
    needed = 0
    for i in range(len(str)):
        if count < i:
            needed += i - count
            count = i
        count += int(str[i])
    return needed

def cases():
    for i in range(1, int(sys.stdin.readline()) + 1):
        max, str = sys.stdin.readline().strip().split(" ")
        print "Case #%d: %d" % (i, ovation(str))

cases()
