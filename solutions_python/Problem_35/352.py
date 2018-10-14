#!/usr/bin/python

import sys

t = int(sys.stdin.readline())

h, w = 0, 0
for case in xrange(1,t+1):
    basin = ord('a')
    (h, w) = map( int, sys.stdin.readline().split(' ') )
    data = []
    output = []
    for y in xrange(0, h):
        data.append(map( int, sys.stdin.readline().split(' ')))

    for y in xrange(0, h):
        output.append([''] * w)

    for y in xrange(0, h):
        for x in xrange(0, w):

            # lowest relative to current cell
            #
            cy, cx = y, x
            cbasin = basin
            backtrack = []
            while (True):
                lowy, lowx = cy, cx
                low = -1
                low_count = 0
                same = True
                neighbours = []
                if output[cy][cx] != '':
                    cbasin = 0 # force don't increase!
                    break

                if cy-1>=0: neighbours.append((cy-1, cx))
                if cx-1>=0: neighbours.append((cy, cx-1))
                if cx+1<w:  neighbours.append((cy, cx+1))
                if cy+1<h:  neighbours.append((cy+1, cx))

                for (n_y, n_x) in neighbours:
                    if (low == -1 and data[n_y][n_x] < data[cy][cx]) or data[n_y][n_x] < low:
                        low = data[n_y][n_x]
                        lowy, lowx = n_y, n_x

                if low == -1: # can't go anywhere
                    output[cy][cx] = chr(cbasin)
                    break # next

                if output[lowy][lowx] != '': # some thing is there already
                    cbasin = ord(output[lowy][lowx])
                    output[cy][cx] = chr(cbasin)
                    for (bt_y, bt_x) in backtrack:
                        output[bt_y][bt_x] = chr(cbasin)
                    break # done

                output[cy][cx] = chr(cbasin)
                backtrack.append((cy, cx))
                cy, cx = lowy, lowx

            if cbasin == basin:
                basin+=1

    print "Case #%d: " % case
    for y in xrange(0, h):
        print ' '.join(map(str,output[y]))
        
