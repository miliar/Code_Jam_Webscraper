#!/usr/bin/env python
from __future__ import with_statement
#from collections import defaultdict

def processFile(fname):
    def processCase(f):
        tc = f.readline().strip("\n").split(" ")
        return setup_robots(tc)
        
    with open(fname, "r") as f:
        cases = int(f.readline().strip("\n"))
        output = ""
        for case in range(cases):
            a = processCase(f)
            output += "Case #%d: %s\n" % (case + 1, a)
        print output
    with open("ans"+fname, "w") as f:
        f.write(output)

def convert_testcase_to_lists(tc):
    buttons = {"O":[], "B":[]}
    step = 0
    while tc:
        color = tc.pop(0)
        button = int(tc.pop(0))
        buttons[color].append((button, step))
        step += 1
    return buttons

def setup_robots(testcase):
    no_steps = int(testcase.pop(0))
    buttons = convert_testcase_to_lists(testcase)
    robots = {}
    for k in buttons:
        robots[k] = Robot(k, buttons[k])
    step = 0
    time = 0
    while step < no_steps:
        for robot in robots.values():
            robot.move(step)
        for robot in robots.values():
            if robot.pushed_button:
                robot.pushed_button = False
                step += 1
        time += 1
    return time

class Robot(object):
    def __init__(self, name, targetlist):
        self.name = name
        self.targetlist = targetlist
        self.location = 1
        self.pushed_button = False

    def roll_call(self):
        return
        print self.name, self.location, self.pushed_button
    @property
    def target(self):
        return self.targetlist and self.targetlist[0][0]
    @property
    def target_step(self):
        return self.targetlist[0][1]
    def push_button(self):
        self.pushed_button = True
        self.targetlist.pop(0)
    def move(self, step):
        if not self.target:
            return
        if self.location == self.targetlist[0][0]:
            if step == self.targetlist[0][1]:
                self.push_button()
        else:
            if self.location > self.target:
                self.location -= 1
            else:
                self.location += 1
        self.roll_call()

#processFile("maze.txt")
#processFile("sample.txt")
#processFile("A-small-attempt0.in")
processFile("A-large.in")