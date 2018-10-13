#!/usr/bin/env python

import sys

def recycled_numbers(a, b):
    recycled = {}

    for i in xrange(a, b + 1):
        for j in xrange(i + 1, b + 1):
            str_i = str(i)
            str_j = str(j)

            if len(str_i) == len(str_j):
                for k in xrange(1, len(str_i)):
                    mod_j = "%s%s" % (str_j[k * -1:], str_j[:k * -1])

                    if str_i == mod_j:
                        lowest = min(i, j)
                        highest = max(i, j)

                        recycled["%s %s" % (lowest, highest)] = True

    return len(recycled)

if __name__ == "__main__":
    lines = int(sys.stdin.readline())

    for i in xrange(lines):
        line = sys.stdin.readline()

        tokens = line.split(' ')

        a = int(tokens[0])
        b = int(tokens[1])

        print "Case #%d: %d" % (i + 1, recycled_numbers(a, b))
