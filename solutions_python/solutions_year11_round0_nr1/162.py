#!/usr/bin/env python

import fileinput

for i, line in enumerate(fileinput.input()):
    if i == 0: continue

    stuff = line.split(' ')[1:]

    time = 0
    times = [0, 0]
    positions = [1, 1]

    while stuff:
        bot, pos = stuff[0:2]
        pos = int(pos)
        stuff = stuff[2:]

        if bot == 'O': bot = 0
        else: bot = 1

        time = max(time, times[bot]+abs(positions[bot]-pos))+1
        times[bot] = time
        positions[bot] = pos

    print "Case #%d: %d" % (i, time)
