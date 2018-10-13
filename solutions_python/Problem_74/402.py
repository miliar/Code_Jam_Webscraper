#!/usr/bin/env python
from collections import namedtuple

def main(argv):
    # Parsing our file
    assert(len(argv) == 2)
    fname = argv[1]
    lines = None
    with open(fname) as fd:
        lines = fd.readlines()
    if not lines:
        return
    lines = lines[1:]
    lines = [line.split()[1:] for line in lines]

    # Starting the simulation
    for testid, test in enumerate(lines, start=1):
        # Token creation
        sequence = []
        for idx in range(0, len(test), 2):
            robot, btn = test[idx:idx+2]
            sequence.append((robot, int(btn)))
        # Our nice little robots
        O = {'position': 1, 'time':0}
        B = {'position': 1, 'time':0}
        actors = {'O': O, 'B': B}
        gametime = 0
        for robot, position in sequence:
            deltapos = abs(position - actors[robot]['position'])
            deltatime = gametime - actors[robot]['time']
            if deltatime > deltapos:
                wait_time = 0
            else:
                wait_time = deltapos - deltatime
            gametime += wait_time + 1
            actors[robot]['position'] = position
            actors[robot]['time'] = gametime
        print "Case #%s: %d" % (testid, gametime)

if __name__ == "__main__":
    import sys
    main(sys.argv)

