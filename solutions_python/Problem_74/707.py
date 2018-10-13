#!/usr/bin/env python

import sys
import select
import collections

try:
    try:
        data = open(sys.argv[1])
    except:
        data = sys.stdin
    if select.select([data,],[],[],0.0)[0]:
        lines = data.readlines()
    T = int(lines[0])
except:
    sys.exit('Usage: %(file)s input-filename' % dict(file=__file__))


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def push_the_buttons_return_seconds(Tcase):
    '''Push the buttons, return time it took in seconds'''
    buttons = {}
    buttons['O'] = collections.deque(int(t[1]) for t in Tcase if t[0]=='O')
    buttons['B'] = collections.deque(int(t[1]) for t in Tcase if t[0]=='B')

    Tcase = collections.deque(Tcase)

    pos = dict(O=1, B=1)

    seconds_passed = 0

    while Tcase:
        pushed = False
        for robot in ('O', 'B'):
            # buttons left to push?
            if not buttons[robot]:
                continue
            # can push the button?
            if (robot, pos[robot]) == Tcase[0]:
                pushed = True
                buttons[robot].popleft()
            else:
                # move in the direction of next button, or stay at the button
                pos[robot] += int(sign(buttons[robot][0] - pos[robot]))
        if pushed:
            Tcase.popleft()
        seconds_passed += 1

    return seconds_passed
    

for t in xrange(1, T+1):
    line = lines[t].split()
    Tcase = [(robot, int(position)) for robot, position in zip(*[iter(line[1:2*int(line[0])+1])]*2)]
    print 'Case #%(case)d: %(time)d' % dict(case=t, time=push_the_buttons_return_seconds(Tcase))
