#!/usr/bin/env python

from sys import argv

def bot_time(seq):
    time = 0
    total = 0
    last_robot = None
    pos = {'O' : 1, 'B': 1}

    for robot,button in seq:
        diff = button - pos[robot]
        robot_changed = last_robot and last_robot != robot
        # Update last robot color
        last_robot = robot
        # Update position
        pos[robot] = button

        if not robot_changed:
            time = time + abs(diff) + 1
        # Already on position
        elif time != 0 and time >= abs(diff):
            diff = 0
            time = 1
        else:
            if diff < 0:
                diff = diff + time
            else:
                diff = diff - time
            # No accumulated time remaining
            time = abs(diff) + 1
        # Not in position, so walk and press the button
        total = total + abs(diff) + 1
    return total

if __name__ == "__main__":
    with open(argv[1], "r") as f:
        cases = int(f.readline())
        for i in range(cases):
            line = f.readline().split()
            buttons = int(line[0])
            seq = []
            for j in range(buttons):
                seq.append((line[2 * j + 1], int(line[2 * j + 2])))
            print "Case #%d: %d" % (i + 1, bot_time(seq))
