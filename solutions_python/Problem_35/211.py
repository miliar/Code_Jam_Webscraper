#!/usr/bin/pyhon

import sys
import re

""" usage: python task_b.py input_file_name

Requires python 2.x
"""

def update(x, y, basins, dirs):
    if (x > 0):
        if dirs[y][x - 1] == 'e':
            basins[y][x - 1] = basins[y][x]
            update(x - 1, y, basins, dirs)
    if (x < len(dirs[y]) - 1):
        if dirs[y][x + 1] == 'w':
            basins[y][x + 1] = basins[y][x]
            update(x + 1, y, basins, dirs)
    if (y > 0):
        if dirs[y - 1][x] == 's':
            basins[y - 1][x] = basins[y][x]
            update(x, y - 1, basins, dirs)
    if (y < len(dirs) - 1):
        if dirs[y + 1][x] == 'n':
            basins[y + 1][x] = basins[y][x]
            update(x, y + 1, basins, dirs)
            
f = open(sys.argv[1])
maps = int(f.readline())
for case_no in range(1, maps + 1):
    line = f.readline()
    (h, w) = [int(s) for s in line.split(' ')]
    a = []
    basins = []
    dirs = []
    for r in range(h):
        line = f.readline()
        alt_row = [int(s) for s in line.split(' ')]
        a.append(alt_row)
        basins.append([0 for x in alt_row])
        dirs.append(['?' for x in alt_row])
    basin = 1
    for y in range(h):
        for x in range(w):
            dn = 0
            ds = 0
            de = 0
            dw = 0
            my_alt = a[y][x]
            if (x > 0):
                if (a[y][x - 1] < my_alt):
                    dw = my_alt - a[y][x - 1]
            if (x < w - 1):
                if (a[y][x + 1] < my_alt):
                    de = my_alt - a[y][x + 1]
            if (y > 0):
                if (a[y - 1][x] < my_alt):
                    dn = my_alt - a[y - 1][x]
            if (y < h - 1):
                if (a[y + 1][x] < my_alt):
                    ds = my_alt - a[y + 1][x]
            max_d = max([dn, ds, de, dw])
            if max_d == 0:
                basins[y][x] = basin
                basin += 1
            else:
                if dn == max_d:
                    dirs[y][x] = 'n'
                elif dw == max_d:
                    dirs[y][x] = 'w'
                elif de == max_d:
                    dirs[y][x] = 'e'
                else:
                    dirs[y][x] = 's'
                    
    #print a, basins, dirs
    for y in range(h):
        for x in range(w):
            if dirs[y][x] == '?':
                update(x, y, basins, dirs)

    labels = {}
    label = 'a'
    for y in range(h):
        for x in range(w):
            n = basins[y][x]
            if not (n in labels.keys()):
                labels[n] = label
                label = chr(ord(label) + 1)
                

    print "Case #%d:" % case_no
    for y in range(h):
        for x in range(w):
            print labels[basins[y][x]],
        print
            
   