#!/usr/bin/env python
# encoding: utf-8
"""
b.py

Created by Robert Wallis on 2009-09-02.
Copyright (c) 2009 Robert Wallis. All rights reserved.
"""
import sys
T = input()

def zero(x):
    return 0

def next_label(x=None):
    global label_counter
    label_counter += 1
    return label_counter

def trickle(sx, sy, dx, dy):
    global label_map, label_counter, direction_map, H, W
    if (label_map[sy][sx] is not 0) and (label_map[sy][sx] == label_map[dy][dx]):
        # we already trickled here
        return
    if label_map[dy][dx] is not 0:
        if label_map[sy][sx] is not 0:
            # make us their river
            old_label = label_map[sy][sx]
            for y in range(0, H):
               for x in range(0, W):
                   if label_map[y][x] == old_label:
                       label_map[y][x] = label_map[dy][dx]
        else:
            # become a tributary
            label_map[sy][sx] = label_map[dy][dx]
    elif label_map[sy][sx] == 0:
        # become the source
        label_map[dy][dx] = label_map[sy][sx] = next_label()
    else:
        # flow into the parched valley
        label_map[dy][dx] = label_map[sy][sx]
            
    #sys.stderr.write("%d,%d flowed %s to %d,%d label %d\n" % (sx, sy, direction_map[sy][sx], dx, dy, label_map[sy][sx]))
    #sys.stderr.write("map: %s\n" % label_map)
    flow(dx, dy)

def flow(x, y):
    global label_map, label_counter, direction_map
    if direction_map[y][x] == "S":
        trickle(x, y, x, y+1)
    elif direction_map[y][x] == "E":
        trickle(x, y, x+1, y)
    elif direction_map[y][x] == "W":
        trickle(x, y, x-1, y)
    elif direction_map[y][x] == "N":
        trickle(x, y, x, y-1)
    else:
        # always will stop at a sink
        if label_map[y][x] == 0:
            label_map[y][x] = next_label()
        #sys.stderr.write("flowed into sink: %d,%d\n" % (x, y))

for case in range(1, T+1):
    print('Case #%d:' % case)
    sys.stderr.write("\n=============================\nCase #%d:\n" % case)
    H, W = map(int, raw_input().split())
    #print "%dx%d:" % (H, W)
    
    label_counter = 0
    height_map = []
    direction_map = []
    label_map = []
    for h in range(1, H+1):
        height_map.append(map(int, raw_input().split()))
        direction_map.append(map(zero, range(0, W)))
        label_map.append(map(zero, range(0, W)))
    for h in height_map:
        sys.stderr.write("%s\n" % h)
    
    # apply gravity and figure out just directions
    for y in range(0, H):
        for x in range(0, W):
            direction = ""
            lowest =  height_map[y][x] - 1 # because of a<=lowest's "=" later
            # south
            if y < H-1:
                a = height_map[y+1][x]
                if a <= lowest:
                    direction = "S"
                    lowest = a
            # east
            if x < W-1:
                a = height_map[y][x+1]
                if a <= lowest:
                    direction = "E"
                    lowest = a
            # west
            if x > 0:
                a = height_map[y][x-1]
                if a <= lowest:
                    direction = "W"
                    lowest = a
            # north
            if y > 0:
                a = height_map[y-1][x]
                if a <= lowest:
                    direction = "N"
                    lowest = a
            #sys.stderr.write("Gravity %d,%d %s lowest:%d\n" % (x, y, direction, lowest))
            direction_map[y][x] = direction
            
    for h in direction_map:
        sys.stderr.write("%s\n" % h)

    # flow in the designated direction
    for y in range(0, H):
        for x in range(0, W):
            # already processed
            if label_map[y][x] is not 0:
                continue
            
            # flow in the designated direction
            flow(x, y)
    # cleanup un-labeled sinks
    for y in range(0, H):
        for x in range(0, W):
            if label_map[y][x] == 0:
                sys.stderr.write("%d,%d was unlabeled\n" % (x,y))
                label_map[y][x] = next_label()
    # get possible labels
    letters = dict()
    for y in range(0, H):
        for x in range(0, W):
            letters[label_map[y][x]] = None
    # assign letters to labels
    current_label = ord('a')
    for l in letters:
        letters[l] = chr(current_label)
        current_label += 1
    # apply letters
    for y in range(0, H):
        for x in range(0, W):
            label_map[y][x] = letters[label_map[y][x]]
    # output answer
    for row in label_map:
        print (" ".join(row))
