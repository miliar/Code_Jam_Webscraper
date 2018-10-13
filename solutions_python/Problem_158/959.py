#!/usr/local/bin/python

import sys


def read_input(filepath):
    f = open(filepath, 'r')
    cases = f.readline()
    for x in xrange(1, int(cases)+1):
        solve_prob(x, f.readline().rstrip())


def solve_prob(case, line):
    RICHARD = 'RICHARD'
    GABRIEL = 'GABRIEL'

    X, R, C = line.split(' ')
    X, R, C = int(X), int(R), int(C)
    area = R * C
    X = int(X)
    if area % X != 0:
        result = RICHARD
    else:
        if R >= (X-1) and C >= (X-1):
            result = GABRIEL
        else:
            result = RICHARD

    print "Case #%d: %s" % (case, result)


def main():
    if (len(sys.argv) < 2):
        sys.exit("usage: blabla")

    read_input(sys.argv[1])


if __name__ == '__main__':
    main()
