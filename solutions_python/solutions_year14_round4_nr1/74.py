#!/usr/bin/env python

import sys
import logging
import argparse


def solve(C, S):
    S.sort()
    count = 0
    i = 0
    j = len(S) - 1
    while i < j:
        if S[i] + S[j] <= C:
            count += 1
            i += 1
            j -= 1
        else:
            count += 1
            j -= 1
    if i == j:
        count += 1
    return count

def main(inp, output):
    T = int(next(inp))
    for case in range(1,T+1):
        N, C = [int(x) for x in next(inp).split()]
        S = [int(x) for x in next(inp).split()]
        r = solve(C, S)
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
