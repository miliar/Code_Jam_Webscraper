#!/usr/bin/env python

import sys

filename = sys.argv[1]

class Robot:
    buttons = 0
    def __init__(self):
        self.xpos = 1
        self.time = 0
    def push(self):
        self.time+= 1

switch = {'O':'B', 'B':'O'}

with open(filename, 'r') as fr:
    cases = int(fr.readline()[:-1])
    for case in xrange(cases):
        orange = Robot()
        blue = Robot()
        robot = {'O':orange, 'B':blue}
        line = fr.readline()[:-1].split()
        Robot.buttons = int(line.pop(0))
        for i, label in enumerate(line[::2]):
            index = i * 2 + 1
            timeNeeded = abs(int(line[index]) - robot[label].xpos)
            catchUp = 0
            if (robot[label].time < robot[switch[label]].time):
                catchUp = robot[switch[label]].time - robot[label].time
            robot[label].time+= timeNeeded if (timeNeeded > catchUp) else catchUp
            robot[label].xpos = int(line[index])
            Robot.buttons-= 1
            robot[label].push()
        else:
            t = orange.time if (orange.time > blue.time) else blue.time
            print "Case #{0}: {1}".format(case+1, t)