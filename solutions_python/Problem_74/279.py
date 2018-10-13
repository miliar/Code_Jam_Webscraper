#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

rl = lambda: sys.stdin.readline().strip()

cases = int(rl())
for cc in xrange(cases):
    seq = rl().split()
    last_time = {"O": 0, "B": 0}
    cur_loc = {"O": 1, "B": 1}
    ctime = 0
    for color, loc in zip(seq[1::2], map(int,seq[2::2])):
        #print loc, color
        dist = abs(cur_loc[color] - loc)
        can_use = ctime - last_time[color]
        #print "dist %d can_use %d" % (dist, can_use)
        cur_loc[color] = loc
        spent = max(0, dist - can_use)
        ctime += spent + 1
        last_time[color] = ctime
    print "Case #%d: %d" % (cc+1, ctime)

