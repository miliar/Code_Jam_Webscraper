#!/usr/bin/env python
# Python 2.6.6

import itertools

t = int(raw_input())

def next_batch(cmds):
    robot = cmds[0][0]
    return (list(itertools.dropwhile(lambda cmd: cmd[0] == robot, cmds)),
            list(itertools.takewhile(lambda cmd: cmd[0] == robot, cmds)))

def solve(cmds):
    o = 1
    b = 1
    total_time = 0
    batch_time = 0
    while cmds:
        (cmds, batch) = next_batch(cmds)
        if batch[0][0] == 'O':
            start = o
            o = batch[len(batch)-1][1]
        else:
            start = b
            b = batch[len(batch)-1][1]
        first_step = max(abs(batch[0][1] - start) - batch_time + 1, 1)
        other_steps = sum(abs(batch[i+1][1] - batch[i][1]) + 1 for i in xrange(len(batch) - 1))
        batch_time = first_step + other_steps
        total_time += batch_time
    return total_time

for i in xrange(1, t+1):
    cmds = raw_input().split()
    n = int(cmds[0])
    cmds = [(cmds[j], int(cmds[j+1])) for j in xrange(1, n * 2, 2)]
    print("Case #%d: %d" % (i, solve(cmds)))
