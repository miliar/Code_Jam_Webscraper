#!/usr/bin/env python

import os, sys, math

def isPalindrome (num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False

def isSquare (num):
    sr = math.sqrt(num)
    if sr == int(sr):
        if isPalindrome(int(sr)):
            return True
    return False

def solve (line):
    start, end = [int(x) for x in line.split(" ")]

    cnt = 0
    for num in xrange(start, end+1):
        if isPalindrome(num) and isSquare(num):
            cnt += 1
    return cnt


fd = sys.stdin

line = fd.readline()
sets = int(line)+1

for case in range(1, sets):
    line = fd.readline().strip()
    nline = solve(line)
    print "Case #%s: %s" % (case, nline)

fd.close()
