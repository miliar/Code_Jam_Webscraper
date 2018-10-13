#!/usr/bin/env python

import sys
import logging
import argparse


def solve(ns, ks):
    ns.sort()
    ks.sort()

    war = 0

    i = 0
    j = len(ks) - 1

    for n in reversed(ns):
        if ks[j] > n:
            j -= 1
        else:
            war += 1
            i += 1

    deceipt = 0
    i = 0
    j = len(ks) - 1
    for n in ns:
        if n < ks[i]:
            # sacrifice...
            j -= 1
        else:
            deceipt += 1
            i += 1

    return "%s %s" % (deceipt, war)


def main(inp, output):
    T = int(next(inp))
    for case in range(1,T+1):
        N = int(next(inp))
        n = [float(x) for x in next(inp).split()]
        k = [float(x) for x in next(inp).split()]
        r = solve(n, k)
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
