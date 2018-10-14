#!/usr/bin/env python

import sys

line = sys.stdin.readline()
nbCase = int(line)
for noCase in xrange( 1, nbCase + 1 ):
    line = sys.stdin.readline()
    line = line.split()
    buttons = []
    for i in xrange(int(line.pop(0))):
        r = line.pop(0)
        b = int(line.pop(0))
        buttons.append( { 'robot':r, 'button':b } )

    s = 0
    o = 1
    b = 1
    while( len(buttons) > 0 ):
        nbut = buttons[0]
        no = nb = None
        for but in buttons:
            if not no and but['robot'] == 'O':
                no = but['button']
            if not nb and but['robot'] == 'B':
                nb = but['button']
            if no and nb:
                break
        if no > o:
            o += 1
        elif no < o:
            o -= 1
        elif nbut['robot'] == 'O':
            buttons.pop(0)
        if nb > b:
            b += 1
        elif nb < b:
            b -= 1
        elif nbut['robot'] == 'B':
            buttons.pop(0)
        s += 1

    print 'Case #' + str(noCase) + ': ' + str(s)
