#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math

def ispalin(num):
    s = str(num)
    l = len(s)
    for i in xrange(0,l):
        if s[i] != s[l - i - 1]:
            return False
    return True
def main():
    count = int(sys.stdin.readline())
    for i in xrange(1,count + 1):
        down,up = sys.stdin.readline().split(' ')
        down = int(down)
        up = int(up)
        sqdown = int(math.floor(math.sqrt(down)))
        squp = int(math.ceil(math.sqrt(up)))
        c = 0
        for j in xrange(sqdown - 1,squp + 1):
            if ispalin(j) and ispalin(j * j) and j*j >= down and j * j <= up:
                c += 1
        sys.stdout.write("Case #%d: %d"%(i,c))
        if i != count:
            sys.stdout.write("\n")

if __name__ == '__main__':
    main()