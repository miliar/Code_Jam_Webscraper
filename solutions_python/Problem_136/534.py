#!/usr/bin/env python

import sys
import logging
import argparse


def solve(C, F, X):

    i = 1
    best = 1e99
    time = 0
    while True:
        t = time + X / (2.0 + (i - 1) * F)
        print i, t
        if t < best:
            best = t
        else:
            break
        time = time + C / (2.0 + (i - 1) * F)
        i += 1

    return "%.7f" % best


def main(inp, output):
    T = int(next(inp))
    for case in range(1,T+1):
        C, F, X = [float(x) for x in next(inp).split()]
        r = solve(C, F, X)
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
