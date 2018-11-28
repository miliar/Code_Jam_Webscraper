#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Qualification Round A
Author: Matt Giuca
"""

import sys

def parse_input(infile):
    """Consume input for a single case from infile.
    Return or yield a data structure describing the input.
    """
    items = infile.readline().split()
    num_items = int(items[0])
    assert num_items*2 == len(items)-1
    for i in range(num_items):
        yield items[i*2+1], int(items[i*2+2])

class Robot:
    def __init__(self, name, pos=1, goal=None):
        self.name = name
        self.pos = pos
        self.goal = goal

    def __repr__(self):
        return "Robot({0}, {1}, {2})".format(self.name, self.pos, self.goal)

    def set_goal(self, commands):
        """Set the robot's goal based on the global command list.
        This sets the robot's goal to its next command in the list.
        @param commands: The global list of commands (in reverse).
        """
        for com in reversed(commands):
            if com[0] == self.name:
                self.goal = com[1]
                return
        # No remaining commands for this robot. Do nothing.
        self.goal = None

    def update(self, next_command):
        """Update the robot for one second, towards its goal.
        @param next_command: The next command to be issued globally.
            Used to check whether this robot is allowed to push its button (if
            this robot is not allowed to push its button, it just waits).
        @returns: True if the robot pushes a button.
        """
        pushed = False
        if self.goal is None:
            pass
            #desc = "Stay at button {}".format(self.pos)
        else:
            if self.goal == self.pos:
                # Ready to push
                if next_command[0] == self.name:
                    # Not waiting for other robot -- push
                    #desc = "Push button {}".format(self.pos)
                    pushed = True
                else:
                    # Waiting for other robot
                    pass
                    #desc = "Stay at button {}".format(self.pos)
            elif self.goal < self.pos:
                self.pos -= 1
                #desc = "Move to button {}".format(self.pos)
            else:
                self.pos += 1
                #desc = "Move to button {}".format(self.pos)
        # Debug
        #print("{0}: {1} ".format(self.name, desc), end='')
        return pushed

def handle_case(data):
    """Given the data structure returned by parse_input, return the answer as
    a string or stringable value.
    If parse_input is a generator, should manually call list() on data.
    """
    data = list(data)[::-1]     # Reversed list (perform commands from end)
    time = 0
    robots = [Robot("O"), Robot("B")]
    while len(data) > 0:
        time += 1
        # Set each robot's goal based on its next action
        for r in robots:
            r.set_goal(data)
        # Update each robot for this turn; possibly pop from data
        next_command = data[-1]
        #print("{} | ".format(time), end = '')
        for r in robots:
            if r.update(next_command):
                data.pop()
        #print(end = '\n')
    return time

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}: {1}".format(casenum+1, answer))

if __name__ == "__main__":
    sys.exit(main())
