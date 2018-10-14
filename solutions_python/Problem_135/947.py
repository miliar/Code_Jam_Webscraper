#!/usr/bin/env python
# encoding: utf-8

import sys

def main():
    times = int(sys.stdin.readline())
    for case_n in xrange(1, times+1):
        r = int(sys.stdin.readline())
        cards1 = set([map(int, sys.stdin.readline().split()) for i in xrange(4)][r-1])
        r = int(sys.stdin.readline())
        cards2 = set([map(int, sys.stdin.readline().split()) for i in xrange(4)][r-1])
        diff = cards1.intersection(cards2)
        diff_len = len(diff)
        if diff_len == 1:
            print "Case #%d: %d" % (case_n, diff.pop())
        elif diff_len > 1:
            print "Case #%d: Bad magician!" % case_n
        else:
            print "Case #%d: Volunteer cheated!" % case_n

if __name__ == "__main__":
    main()
