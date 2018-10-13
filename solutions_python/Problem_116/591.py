#!/usr/bin/env python

import sys
import logging

def solve(data):
    all_lines = []
    all_lines.extend(x for x in data)
    for c in xrange(4):
        all_lines.append([data[r][c] for r in xrange(4)])
    all_lines.append([data[x][x] for x in xrange(4)])
    all_lines.append([data[3-x][x] for x in xrange(4)])
    for line in all_lines:
        x = line.count("X") + line.count("T")
        o = line.count("O") + line.count("T")
        if x == 4:
            return "X won"
        if o == 4:
            return "O won"
    for row in data:
        if "." in row:
            return "Game has not completed"
    return "Draw"

def main(lines, output):
    T = int(lines.next())
    for case in xrange(1,T+1):
        if case > 1:
            lines.next()
        data = []
        for kk in xrange(4):
            data.append(lines.next().strip())
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

