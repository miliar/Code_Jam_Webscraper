#!/usr/bin/env python


import sys


def solve(a1, c1, a2, c2):
    i = set(c1[a1 - 1]) & set(c2[a2 - 1])
    if len(i) >= 2:
        return "Bad magician!"
    if len(i) == 0:
        return "Volunteer cheated!"
    return "%d" % list(i)[0]


def main():
    with open(sys.argv[1], 'r') as fin:
        T = int(fin.readline().strip())
        for t in xrange(T):
            a1 = int(fin.readline().strip())
            c1 = [map(int, fin.readline().strip().split(" ")) for _ in xrange(4)]
            a2 = int(fin.readline().strip())
            c2 = [map(int, fin.readline().strip().split(" ")) for _ in xrange(4)]
            print "Case #%d: " % (t + 1),
            print solve(a1, c1, a2, c2)
            print


if __name__ == '__main__':
    main()

