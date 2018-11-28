#! /usr/bin/env python

import sys
from collections import defaultdict

if sys.stdin.isatty():
    # Open the file
    #reader = open('mini.in', 'r')
    #reader = open('A-small-attempt0.in', 'r')
    reader = open('A-large.in', 'r')


    for count, line in enumerate(reader):
        if count == 0:
            continue
        
        inputs = line.rstrip().split(" ")
        inputs.pop(0)

        elapsed = 0
        last = defaultdict(lambda: { 'pos': 1,
                                     'time': 0 })

        while inputs:
            color = inputs.pop(0)
            position = int(inputs.pop(0))

            move = abs(last[color]['pos'] - position)
            time = last[color]['time'] + move

            elapsed = (time if time > elapsed else elapsed) + 1
            
            last[color]['time'] = elapsed
            last[color]['pos'] = position
            
        print 'Case #{0}: {1}'.format(count, elapsed)
