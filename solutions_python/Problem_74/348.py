#!/usr/bin/python

import sys

bots = {'B': 0, 'O': 1}

cases = int(sys.stdin.readline().strip())
for case in range(1, cases + 1):
    line = sys.stdin.readline().split()
    N = int(line[0])
    sequence = [(bots[line[2*n+1]], int(line[2*n+2])) for n in range(N)]
    positions = [(1, 0), (1, 0)]
    time = 0
    for (bot, button) in sequence:
        (position, last_time) = positions[bot]
        distance = abs(button - position)
        interval = time - last_time
        if distance > interval:
            #print 'bot %d walking %d steps' % (bot, distance-interval)
            time += distance - interval
        #print 'bot %d pushing button %d' % (bot, button)
        time += 1
        positions[bot] = (button, time)
    print 'Case #%d: %d' % (case, time)


# vim:set ts=4 sw=4 et:
