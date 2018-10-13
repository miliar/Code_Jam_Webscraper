#!/usr/bin/env python
# encoding: utf-8
"""
BotTrust.py

Created by Graham Dennis on 2011-05-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys


def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in xrange(T):
        instructions = f.readline().split()[1:]
        state = {
            'O': (1, 0),
            'B': (1, 0)
        }
        time = 0
        for robot, button in zip(instructions[::2], instructions[1::2]):
            button = int(button)
            loc, lastTime = state[robot]
            time = lastTime = max(time, lastTime + abs(loc - button)) + 1
            state[robot] = button, lastTime
        
        print "Case #%i: %i" % (t+1, time)

if __name__ == "__main__":
    sys.exit(main())
