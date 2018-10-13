#!/usr/bin/env python

import sys
from collections import deque

input = sys.stdin.readlines()
num_cases = int(input[0])
input = input[1:]

class AlreadyAddedEveryone(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return repr('Already added all groups to the coaster')

class GroupManager(object):
    def __init__(self, groups):
        """assumes group is not empty"""
        self.groups = groups
        self.pointer = 0
        self.calls = 0 

    def reset_calls(self):
        self.calls = 0

    def peek(self):
        if self.pointer >= len(self.groups):
            return self.groups[0] 
        return self.groups[self.pointer]

    def next(self):
        self.calls += 1
        if self.calls > len(self.groups):
            raise AlreadyAddedEveryone() 

        if self.pointer >= len(self.groups):
            self.pointer = 0

        value = self.groups[self.pointer] 
        self.pointer += 1
        return value 

for case in range(0,num_cases):
    details = input[case*2].strip().split()
    runs = int(details[0])
    capacity = int(details[1])
    num_groups = int(details[2])

    groups = [int(xx) for xx in input[case*2+1].strip().split()]
    groups = GroupManager(groups) 

    euros = 0
    for run in range(runs):
        full = False
        num_riders = 0
        groups.reset_calls()

        # adding riders to the run
        while not full: 
            if num_riders + groups.peek() <= capacity:
                try:
                    num_riders += groups.next()
                except AlreadyAddedEveryone:
                    euros += num_riders

                    assert num_riders <= capacity
                    break
            else:
                assert num_riders <= capacity
                euros += num_riders
                full = True

    print "Case #%d: %d" % (case+1, euros)
