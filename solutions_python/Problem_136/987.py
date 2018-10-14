#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#file_path = "/Users/flynn/playground/gcj/qualification/b.in"
#file = open(file_path, 'r')
file = sys.stdin

def runner(handler):
    T = int(file.readline())
    for t in xrange(T):
        print "Case #%s:" % (t+1),
        handler()

def run():
    growth = 2.0
    cost, inc, target = map(float, file.readline().split())
    t = target / growth

    wait = .0
    while True:
        wait += cost / growth
        growth += inc
        tmp = wait + target / growth
        if tmp > t:
            break
        #print t, tmp
        t = tmp
    print t

runner(run)
