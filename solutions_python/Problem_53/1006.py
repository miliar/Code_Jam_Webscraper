#!/usr/bin/env python

import sys

line = sys.stdin.readline()
linelist = line.split()
if len(linelist) != 1:
    sys.exit(1)
t = int(linelist[0])

def flip_switch(lights):
    for i in range(len(lights)):
        if lights[i]:
            lights[i] = False
        else:
            lights[i] = True
            break
    return lights

def calc_light(n,k):
    lights = [False]*n
    for i in range(k):
        lights = flip_switch(lights)
    return sum(lights) == len(lights)

for i in range(t):
    line = sys.stdin.readline()
    linelist = line.split()
    if len(linelist) != 2:
        sys.exit(1)
    n = int(linelist[0])
    k = int(linelist[1])
    result = calc_light(n,k)
    if result:
        print "Case #%s: ON" % str(i+1)
    else:
        print "Case #%s: OFF" % str(i+1)
