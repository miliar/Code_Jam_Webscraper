#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def is_max_in_range(num, index):
    max_v = num[index];
    for i in xrange(index):
        if num[i] > max_v:
            return False
    return True

def solve(n):
    num = list(n)
    for i in xrange(len(num)-1, 0, -1):
        if not is_max_in_range(num, i):
            num[i-1] = str(int(num[i-1]) - 1)
            for i in xrange(i, len(num)):
                num[i] = '9'
    return ''.join(num).lstrip("0")

if __name__ == "__main__":
    T = input()
    for t in xrange(1, T+1):
        num = map(str ,sys.stdin.readline().split())
        print "Case #{no}: {result}".format(no=t, result=solve(num[0]))
