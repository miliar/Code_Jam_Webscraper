#! /usr/bin/python

from __future__ import division

import sys

name = "A-large"
path = ""

f = open(name + ".in", 'r')
o = open(name + ".out", 'w')

T = int(f.readline().strip())
sys.setrecursionlimit(1500)

print T
for t in xrange(T):
    (dest,horses) = map(int, f.readline().strip().split(" "))
    print dest
    print horses
    l = []
    for h in xrange(horses):
        (location,speed) = map(int, f.readline().strip().split(" "))
        print location 
        print speed
        time = (dest - location) / speed
        l.append(time)
    max_time = max(l)
    cruise_speed = dest / max_time
    print cruise_speed
        
    #senates = []
    #senates= map(int, f.readline().strip().split(" "))
    res = cruise_speed
    s = "Case #%d: %.6f\n" % (t + 1, res)
    print s
    o.write(s)

