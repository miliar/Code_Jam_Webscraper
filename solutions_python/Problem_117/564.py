#!/usr/bin/env python

import sys
import logging

def solve(data):
    rows = len(data)
    cols = len(data[0])
    row_maxs = [0] * rows
    col_maxs = [0] * cols
    for r in xrange(rows):
        for c in xrange(cols):
            v = data[r][c]
            row_maxs[r] = max(row_maxs[r], v)
            col_maxs[c] = max(col_maxs[c], v)
    for r in xrange(rows):
        for c in xrange(cols):
            # each item must be >= everything in its row or col.
            v = data[r][c]
            if v < row_maxs[r] and v < col_maxs[c]:
                return "NO"
    return "YES"

def main(lines, output):
    T = int(lines.next())
    for case in xrange(1,T+1):
        R, C = [int(x) for x in lines.next().split()]
        data = []
        for ii in xrange(R):
            data.append([int(x) for x in lines.next().split()])
        r = solve(data)
        s = "Case #%d: %s" % (case, r)
        output.write(s + "\n")
        logging.info(s)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "expects filename"
        sys.exit(1)
    logging.basicConfig(level=logging.DEBUG)
    outfile = sys.argv[1] + ".out"
    main(open(sys.argv[1]), open(outfile, "w"))

