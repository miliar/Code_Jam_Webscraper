#!/usr/bin/python

import os, sys

def change_color(tile, r, c):
    ir = len(tile)
    ic = len(tile[0])
    
    if r+1 >= ir or c+1 >= ic:
        return False

    if tile[r][c] != '#' or tile[r][c+1] != '#' or tile[r+1][c] != '#' or tile[r+1][c+1] != '#':
        return False
    
    tile[r][c] = '/'
    tile[r][c+1] = '\\'
    tile[r+1][c] = '\\'
    tile[r+1][c+1] = '/'

    return True

def change(tile):
    ir = len(tile)
    ic = len(tile[0])
    for r in xrange(ir):
        c = 0
        while c < ic:
            # check if it is blue
            if tile[r][c] == '#':
                # change_color(tile, r, c)
                ret = change_color(tile, r, c)
                if not ret:
                    return ret

                c += 1
            c += 1
    return True

def main():
    fin = open(sys.argv[1])
    icase = int(fin.readline().strip())

    for c in xrange(icase):
        ir, ic = map(int, fin.readline().strip().split())
        tile = []
        for r in xrange(ir):
            tile.append(list(fin.readline().strip()))
        ret = change(tile)
        print "Case #%d:" % (c+1)
        if not ret:
            print "Impossible"
        else:
            for r in xrange(ir):
                print ''.join(tile[r])

if __name__ == "__main__":
    main()
