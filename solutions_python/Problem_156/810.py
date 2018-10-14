#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import sys


def solve(num, pans, level, mmap):
    max_pan = max(pans)
    result = 0
    if max_pan > 3:
        pans_copy = pans[:]
        pans_copy.remove(max_pan)
        pans_copy.extend([max_pan/2,max_pan-max_pan/2])
        pans_copy1 = pans[:]
        pans_copy1.remove(max_pan)
        pans_copy1.extend([max_pan/3,max_pan-max_pan/3])
        result = min(max_pan, solve(num+1, pans_copy[:], level+1, mmap)+1, solve(num+1, pans_copy1, level+1, mmap)+1)
    else:
        result += max_pan
    return result

if __name__ == "__main__":
    T = input()
    #mmap = [solve(1, [i], 0, None) for i in xrange(1, 1001)]
    for t in xrange(1, T+1):
        num = int(sys.stdin.readline())
        pans = map(int ,sys.stdin.readline().split())
        print "Case #{no}: {result}".format(no=t, result=solve(num, pans, 0, None))