#!/usr/bin/python

def intread(fd):
    return int(fd.readline().strip('\n'))

class Events():
    def __init__(self, fd):
        """
        read a line with the
        Letter Button ...
        pairs and return a list with (Letter,Button)
        """
        line = fd.readline().split()

        self.N = int(line[0])
        self.events = []
        # Do not worry about the last \n...
        for i in xrange(self.N):
            self.events.append( (line[2*i+1], int(line[2*i+2])) )

        self.nextTask = 0
        self.doNext = False

    def first_task(self, RobotId):
        for j in xrange(self.N):
            if self.events[j][0]==RobotId:
                return j
        return None

    def advance(self, RobotId):
        """
        Advance the task count and return the next task
        for the robot RobotId or None
        """
        self.doNext = True
        for j in xrange(self.nextTask+1, self.N):
            if self.events[j][0]==RobotId:
                return j
        return None

    def tictac(self):
        if self.doNext:
            self.nextTask += 1
            self.doNext = False

    def is_next(self, task):
        return self.nextTask==task

    def get_button(self, task):
        return self.events[task][1]

    def __len__(self):
        return self.N

class Robot():
    def __init__(self, RobotId, events):
        self.RobotId = RobotId
        self.nextTask = events.first_task(RobotId)
        self.position = 1

    def tictac(self, events):
        """
        Simulate wht to do next second, return True if the task is done
        """
        # Something to do?
        if self.nextTask is None:
            # No job to do
            return True
        else:
            button = events.get_button(self.nextTask)

        # Move? Wait? Press?
        if self.position==button:
            if events.is_next(self.nextTask):
                # Press the button and receive next task :)
                self.nextTask = events.advance(self.RobotId)
                return self.nextTask is None
            else:
                # Nothing to do...
                pass
        else:
            # Search the next button!
            delta = button - self.position
            self.position += delta/abs(delta)
        return False

def solve(fd):
    task = Events(fd)

    if len(task)==0:
        return 0
    Orange = Robot('O', task)
    Blue = Robot('B', task)

    okOrange = False
    okBlue = False
    t = 0
    while not (okOrange and okBlue):
        t += 1
        if not okOrange:
            okOrange = Orange.tictac(task)
        if not okBlue:
            okBlue = Blue.tictac(task)
        task.tictac()
    return t


import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = intread(fd)
for i in xrange(T):
    print("Case #%d: %d" % (i+1, solve(fd)))

fd.close()
