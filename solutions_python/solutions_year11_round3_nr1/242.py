#!/usr/bin/python

import sys
import math


def squareTiles(p, row, col):
    for i in range(row):
        for j in range(col):
            if p[i][j] == '.':
                continue
            if p[i][j] == '#':
                if i + 1 < row and j + 1 < col and p[i][j+1] == '#' and p[i+1][j] == '#' and p[i+1][j+1] == '#':
                    p[i][j] =  '/'
                    p[i][j+1] ='\\'
                    p[i+1][j] = '\\'
                    p[i+1][j+1] = '/'
                else:
                    return "Impossible"
    output = ""
    for i in range(row):
        for j in range(col):
            output = output + p[i][j]
        output += '\n'
    return output

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if not len(argv) == 2:
        print >>sys.stderr, "Usage: store-credit.py infile"

    infile = argv[1]
    f = open(infile, 'r')
    N = int(f.readline())

    for i in range(N):
        R, C = map(lambda x: int(x), f.readline().strip().split())
        pic = []
        for j in range(R):
            row = []
            line = f.readline().strip()
            for x in line:
                row.append(x)
            pic.append(row)
        result = squareTiles(pic, R, C)
        print "Case #%d:" % (i + 1)
        print result
        
if __name__ == "__main__":
    sys.exit(main())

