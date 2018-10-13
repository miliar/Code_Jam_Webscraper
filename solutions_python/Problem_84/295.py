#!/usr/bin/env python

def inp():
    return [eval(x) for x in raw_input().strip().split()]

def cover(tile, i, j):
    if tile[i][j] == '#':
        if i+1 >= len(tile) or tile[i+1][j] != '#':
            return False
        elif j+1 >= len(tile[0]) or tile[i][j+1] != '#':
            return False
        elif tile[i+1][j+1] != '#':
            return False
        else:
            tile[i][j] = '/'
            tile[i+1][j] = '\\'
            tile[i][j+1] = '\\'
            tile[i+1][j+1] = '/'
            return True
    else:
        return True

def solveCase():
    r, c = inp()
    rec = []
    for i in range(r):
        rec.append(raw_input().strip())
    tile = [list(s) for s in rec]
    for i in range(r):
        for j in range(c):
            if not cover(tile, i, j):
                return "\nImpossible"
    return "\n" +  "\n".join(["".join(s) for s in tile])

def main():
    [ncase] = inp()
    for i in xrange(ncase):
        print "Case #%d: %s" % (i+1, solveCase())

if __name__ == "__main__":
    main()

