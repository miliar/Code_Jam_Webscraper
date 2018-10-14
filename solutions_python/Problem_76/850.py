#! /usr/bin/env python

import sys

if sys.stdin.isatty():
    # Open the file
    #reader = open('mini.in', 'r')
    reader = open('C-small-attempt0.in', 'r')
    #reader = open('C-large.in', 'r')


    for count, line in enumerate(reader):
        if count % 2 == 1 or count == 0:
            continue
        
        candy = sorted([ int(x) for x in line.split(" ") ], reverse=True)

        if reduce(lambda x, y: x ^ y, candy, 0) == 0:
            length = len( bin( candy[0] ))
            piece = 0
            for index in range(0, len(candy)):
                if length > len( bin( candy[index] )):
                    piece = index if index > 0 else 0

            candy.pop(piece)
            print 'Case #{0}: {1}'.format( count / 2,
                                           reduce(lambda x, y: x + y, candy, 0) )
            
        else:
            print 'Case #{0}: NO'.format(count / 2)
