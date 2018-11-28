#!/usr/bin/env python

from copy import deepcopy
from string import ascii_lowercase
from string import ascii_uppercase
from sys import setrecursionlimit

global themap, newmap

def fall_to(y, x):
    if x < 0 or x >= len(themap[0]) or y < 0 or y >= len(themap):
        return (-1, -1)

    dn = themap[y][x] - themap[y - 1][x] if y > 0 else 0
    ds = themap[y][x] - themap[y + 1][x] if y < len(themap) - 1 else 0
    dw = themap[y][x] - themap[y][x - 1] if x > 0 else 0
    de = themap[y][x] - themap[y][x + 1] if x < len(themap[0]) - 1 else 0

    if dn > 0 and dn == max(dn, dw, de, ds):
        return (y - 1, x)
    if dw > 0 and dw == max(dn, dw, de, ds):
        return (y, x - 1)
    if de > 0 and de == max(dn, dw, de, ds):
        return (y, x + 1)
    if ds > 0 and ds == max(dn, dw, de, ds):
        return (y + 1, x)
    
    return (-1, -1)

def do_fill(y, x, c):
    if x < 0 or x >= len(themap[0]) or y < 0 or y >= len(themap):
        return 0
    if 'a' <= newmap[y][x] <= 'z':
        return 0

    newmap[y][x] = c
    
    if (y, x) == fall_to(y - 1, x):
        do_fill(y - 1, x, c)
    if (y, x) == fall_to(y + 1, x):
        do_fill(y + 1, x, c)
    if (y, x) == fall_to(y, x - 1):
        do_fill(y, x - 1, c)
    if (y, x) == fall_to(y, x + 1):
        do_fill(y, x + 1, c)
    return 0

def min_in_list():
    min_val = newmap[0][0]
    min_index = (0, 0)

    for i in range(len(newmap)):
        for j in range(len(newmap[0])):
            if newmap[i][j] < min_val:
                min_val = newmap[i][j]
                min_index = (i, j)
    try:
        x = int(min_val)
        return min_index
    except ValueError:
        return (-1, -1)

def main():
    setrecursionlimit(20000)

    global themap, newmap
    for testcase in range(input()):
        h, w = [int(i) for i in raw_input().split()]

        themap = [[0] * w] * h
        newmap = [['0'] * w] * h

        for y in range(h):
            themap[y] = [int(i) for i in raw_input().split()]
        newmap = deepcopy(themap)
        
        for c in ascii_uppercase:
            i, j = min_in_list()
            if i == -1 and j == -1:
                break
            do_fill(i, j, c)

        result = []
        for i in range(h):
            for j in range(w):
                if newmap[i][j] not in result:
                    result.append(newmap[i][j])
        
        for k in range(len(result)):
            rep_from = result[k]
            rep_to = ascii_lowercase[k]

            for i in range(h):
                for j in range(w):
                    if newmap[i][j] == rep_from:
                        newmap[i][j] = rep_to
        # output
        print 'Case #%d: ' % (testcase + 1)
        for i in range(h):
            for j in range(w):
                print newmap[i][j],
            print

if __name__ == '__main__':
    main()
