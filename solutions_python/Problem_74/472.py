#!/usr/bin/env python
#
#  Solving Problems
#  ================
#
#  Jose Ignacio Galarza (igalarzab)
#  <igalarzab@gmail.com>
#  http://sysvar.net
#

import sys, re

def solve(movements, debug=False):
    copy = movements[:]
    blue, orange = ([], [])
    mblue, morange = (False, False)
    bpos, opos = (1, 1)
    steps = 0

    # Blue movements
    for i in xrange(len(movements)):
        if movements[i][0] == 'B':
            blue.append(i)

    # Orange movements
    for i in xrange(len(movements)):
        if movements[i][0] == 'O':
            orange.append(i)

    while copy:
        if debug:
            print('==> ' + str(steps))
        # Blue movement
        if blue and bpos < movements[blue[0]][1]:
            bpos += 1
            if debug:
                print('Blue +1')
        elif blue and bpos > movements[blue[0]][1]:
            bpos -= 1
            if debug:
                print('Blue -1')
        else: # ==
            if copy and copy[0][0] == 'B':
                mblue = True
                if debug:
                    print('Blue pulse')

        # Orange movement
        if orange and opos < movements[orange[0]][1]:
            opos += 1
            if debug:
                print('Orange +1')
        elif orange and opos > movements[orange[0]][1]:
            opos -= 1
            if debug:
                print('Orange -1')
        else:
            if copy and copy[0][0] == 'O':
                morange = True
                if debug:
                    print('Orange pulse')

        steps += 1

        if mblue:
            mblue = False
            copy.pop(0)
            blue.pop(0)

        if morange:
            morange = False
            copy.pop(0)
            orange.pop(0)

    return steps

if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        inputt = re.split(r'([\d]+) (.*)', sys.stdin.readline())
        string = [j for j in re.split(r'([O|B] [\d]+)[ ]*', inputt[2]) if j]
        movements = []

        for k in xrange(int(inputt[1])):
            s = string[k].split()
            movements.append((s[0], int(s[1])))

        steps = solve(movements)
        print("Case #%d: %d" % (i+1, steps))

# vim: ai ts=4 sts=4 et sw=4
