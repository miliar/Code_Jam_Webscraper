#!/usr/bin/env python

def solve(line):
    line = line.split()[1:]
    events = zip(line[::2], map(int, line[1::2]))
    time = { 'O': 1, 'B': 1 }
    pos = { 'O': 1, 'B': 1 }

    t = 0
    for colour, button in events:
        t = max(t + 1, abs(button - pos[colour]) + time[colour])
        time[colour] = t + 1
        pos[colour]  = button

    return t

T = int(raw_input())
for t in range(1, T+1):
    print "Case #%d: %d" % (t, solve(raw_input()))
