#!/usr/bin/python

import sys

def rstr(in_file=sys.stdin):
    return in_file.readline().strip()

def rint(in_file=sys.stdin):
    return int(rstr(in_file))

def list_candidates(x, y, w, h):
    candidates = []
    if y > 0:
        candidates.append((x, y-1),)
    if x > 0:
        candidates.append((x-1, y),)
    if x < (w-1):
        candidates.append((x+1, y))
    if y < (h-1):
        candidates.append((x, y+1),)
    #candidates.append((x, y),)
    return candidates
    
def cell_value(the_map, coords):
    return the_map[coords[1]][coords[0]]

def dbg(*x):
    pass

def run():
    n_maps = rint()
    for case in range(n_maps):
        height, width = [int(x) for x in rstr().split()]
        the_map = []
        for row in range(height):
            the_map.append([int (x) for x in rstr().split()])
        # We have the map, organized as a list of rows.
        
        # Build tree.
        down = []
        up = []
        for y in range(len(the_map)):
            down.append([])
            up.append([])
            for x in range(len(the_map[y])):
                down[y].append(False)
                up[y].append([])
        for y in range(len(the_map)):
            for x in range(len(the_map[y])):
                list_cand = list_candidates(x, y, width, height)
                best = (x,y)
                cur_val = cell_value(the_map, best)
                for cand in list_cand:
                    cur_val = cell_value(the_map, best)
                    cand_val = cell_value(the_map, cand)
                    if cand_val < cur_val:
                        best = cand
                down[y][x] = best
                if best == (x, y):
                    pass
                else:
                    up[best[1]][best[0]].append((x, y),)
        
        # Now we have edges in both directions.
        available_labels = 'abcdefghijklmnopqrstuvwxyz'
        labels = []
        for y in range(len(the_map)):
            labels.append([])
            for x in range(len(the_map[y])):
                labels[y].append(False)
        for y in range(len(the_map)):
            for x in range(len(the_map[y])):
                if labels[y][x] == False:
                    # Pick a new label
                    current_label = available_labels[0]
                    available_labels = available_labels[1:]
                    # Find valley
                    cur = (x, y)
                    prev = None
                    while cur != prev:
                        prev = cur
                        cur = down[cur[1]][cur[0]]
                    # Climb and relabel
                    labels[cur[1]][cur[0]] = current_label
                    climbable = up[cur[1]][cur[0]]
                    while len(climbable):
                        cur = climbable[0]
                        labels[cur[1]][cur[0]] = current_label
                        climbable = climbable[1:]
                        climbable.extend(up[cur[1]][cur[0]])
        # Output
        print 'Case #%s:' % (case+1)
        for label_row in labels:
            print ' '.join(label_row)
        
run()
                    
                        
            