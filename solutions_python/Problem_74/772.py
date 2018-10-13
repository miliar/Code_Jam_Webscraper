#!/usr/bin/python2.6.6

from collections import deque
from os.path import basename
import sys

def move(bots, bot_step):
    bot, pos = bot_step
    # print "Bot %s moves toward %s." % bot_step
    if bots[bot] > pos:
        bots[bot] -= 1
    elif bots[bot] < pos:
        bots[bot] += 1

def push(bot_step, steps, bot_steps):
    bot, pos = bot_step
    # print "Bot %s pushes at %s." % bot_step
    steps.remove(bot_step)
    bot_steps[bot].popleft()


problem = basename(sys.argv[0]).split('.')[0]
infile = file('in/' + '-'.join((problem, sys.argv[1])) + '.in')
outfile = file('out/' + '-'.join((problem, sys.argv[1])) + '.out', 'w')

cases = xrange(int(infile.readline().strip()))
for case in cases:
    line = deque(infile.readline().strip().split())
    
    time, bots = 0, {'B': 1, 'O': 1}
    steps, bot_steps = deque(), {'B': deque(), 'O': deque()}
    
    for step in xrange(int(line.popleft())):
        robot, pos = line.popleft(), int(line.popleft())
        steps.append((robot, pos))
        bot_steps[robot].append(pos)

    while not len(steps) == 0:
        time += 1
        
        # Where's this robot going?
        this = steps[0]

        # Where's that robot going?
        that = 'B'
        if this[0] == 'B':
            that = 'O'
       
        if len(bot_steps[that[0]]):
            that = (that[0], bot_steps[that[0]][0])
        else: that = (that[0], None)

        # If this robot is here, push the button and try to move that robot.
        if bots[this[0]] == this[1]:
            push(this, steps, bot_steps)
            move(bots, that)

        # Otherwise, move this robot and that robot.
        else:
            move(bots, this)
            move(bots, that)

    result = 'Case #%d: %d' % (case+1, time)
    print result
    outfile.write(result + "\n")

infile.close()
if outfile is not None:
    outfile.close()
