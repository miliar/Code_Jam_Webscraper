#!/usr/bin/env python

import sys

ORANGE, BLUE = 0, 1

class Hallway(object):
    
    def __init__(self):
        self.position = [1, 1]
        self.last_moved = [0, 0]
        self.time = 0

    def move_and_press(self, robot, to):
        # +1 for pressing the button
        time_required = abs(to - self.position[robot]) + 1
        # We can use the past to our advantage, but need to spend at least 1
        # tick to press the button
        self.time += max(1, time_required - (self.time - self.last_moved[robot]))
        self.last_moved[robot] = self.time
        self.position[robot] = to


def main(fp=sys.stdin):
    fp.readline()
    case = 1
    for line in fp:
        hallway = Hallway()
        parts = line.split()
        for robot, button in zip(parts[1::2], map(int, parts[2::2])):
            hallway.move_and_press(ORANGE if robot == 'O' else BLUE, button)
        print 'Case #%d: %d' % (case, hallway.time)
        case += 1    

if __name__ == '__main__':
    main()
