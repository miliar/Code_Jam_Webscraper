#!/usr/bin/env python

import sys


def solve(counts):
    invited = 0
    standing = 0
    for shyness, count in enumerate(counts):
        if standing < shyness:
            missing = shyness - standing
            invited += missing
            standing += missing
        standing += count
    return invited


def main():
    lines = sys.stdin.readlines()
    tests = int(lines[0])
    for i in xrange(tests):
        smax, counts = lines[i + 1].split()
        counts = [int(d) for d in counts]
        print "Case #%d: %d" % (i + 1, solve(counts))


if __name__ == "__main__":
    main()
