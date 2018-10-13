#!/usr/bin/python2

from __future__ import print_function

class Robot():
    def __init__(self):
        self.pos = 1
        self.last_time = 0


with open("input.txt") as f:
    lines = f.readlines()
    lines.pop(0)
    n_line = 0
    for line in lines:
        n_line += 1
        orange = Robot()
        blue = Robot()
        time = 0

        moves = line.split()
        moves.pop(0)
        n = 0

        while n < len(moves):
            r = blue if moves[n] == 'B' else orange
            next_step = int(moves[n+1])
            move_time = abs(next_step - r.pos)
            waste_time = move_time - (time - r.last_time)
            waste_time = 0 if waste_time < 0 else waste_time
            time += waste_time + 1
            r.pos = next_step
            r.last_time = time
            n += 2
        
        print("Case #%d: %d" % (n_line, time))
