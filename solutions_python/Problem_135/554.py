#!/usr/bin/env python

import sys
import logging
import argparse


def solve(g1, lines1, g2, lines2):
    f = set(lines1[g1 - 1])
    g = set(lines2[g2 - 1])
    u = f.intersection(g)
    if not u:
        return "Volunteer cheated!"
    elif len(u) > 1:
        return "Bad magician!"

    else:
        return u.pop()

def main(inp, output):
    T = int(next(inp))
    for case in range(1,T+1):
        g1 = int(next(inp))
        lines1 = []
        for k in xrange(4):
            lines1.append([int(x) for x in next(inp).split()])
        g2 = int(next(inp))
        lines2 = []
        for k in xrange(4):
            lines2.append([int(x) for x in next(inp).split()])
        r = solve(g1, lines1, g2, lines2)
        s = "Case #%d: %s" % (case, r)
        print(s)
        output.write(s + "\n")
        logging.info(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="run code jam problem")
    parser.add_argument("filename", type=str, help="input filename")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="enable verbose logging")

    args = parser.parse_args()
    if args.verbose:
        level=logging.DEBUG
    else:
        level=logging.INFO
    logging.basicConfig(level=level,
                        filename="logfile.txt",
                        filemode="w")
    outfile = args.filename + ".out"

    with open(args.filename) as inp:
        with open(outfile, "w") as outp:
            main(inp, outp)
