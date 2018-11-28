#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


#file_path = "/Users/flynn/playground/gcj/qualification/d.in"
#file = open(file_path, 'r')
file = sys.stdin

def runner(handler):
    T = int(file.readline())
    for t in xrange(T):
        print "Case #%s:" % (t+1),
        handler()

def cheat(n, naomi, ken):
    j, cnt = 0, 0
    for i in xrange(n):
        if naomi[i] > ken[j]:
            cnt += 1
            j += 1
    return cnt

def normal(n, naomi, ken):
    j, cnt = n-1, 0
    for i in xrange(n-1, -1, -1):
        if naomi[i] > ken[j]:
            cnt += 1
        else:
            j -= 1
    return cnt

def run():
    n = int(file.readline())
    naomi = sorted(map(float, file.readline().split()))
    ken = sorted(map(float, file.readline().split()))

    print cheat(n, naomi, ken), normal(n, naomi, ken)
    #print naomi
    #print ken

runner(run)
