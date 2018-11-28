#!/usr/bin/env python

import sys

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
T = int(raw_input())  # read a line with a single integer
for t in xrange(1, T + 1):
    r, c = raw_input().split(" ")
    r = int(r)
    c = int(c)

    cake = []
    location = {}
    for row in xrange(r):
        line = list(raw_input())
        cake.append(line)
        contains = []
        for col in xrange(c):
            if line[col] != '?':
                contains.append(col)
        if len(contains) > 0:
            location[row] = contains

    # print cake
    # print location

    row_begin = 0
    for row in xrange(r):
        if location.has_key(row):
            row_end = row + 1
            while row_end < r and not location.has_key(row_end):
                row_end += 1

            col_begin = 0
            for col_end in location[row]:
                for rr in xrange(row_begin, row_end):
                    for cc in xrange(col_begin, col_end + 1):
                        cake[rr][cc] = cake[row][col_end]
                col_begin = col_end + 1
            col_begin = location[row][-1]
            col_end = c - 1
            for rr in xrange(row_begin, row_end):
                for cc in xrange(col_begin, col_end + 1):
                    cake[rr][cc] = cake[row][col_begin]

            row_begin = row + 1


    print "Case #{}:".format(t)
    for row in xrange(r):
        for col in xrange(c):
            sys.stdout.write(cake[row][col])
        print ""
