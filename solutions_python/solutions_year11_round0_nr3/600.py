#!/usr/bin/python2.7

import sys

sean_add = lambda x, y: x + y
patric_add = lambda x, y: x ^ y
sean_sum = lambda s: sum(s)
patric_sum = lambda s: reduce(patric_add, s, 0)

def find_solutions(values, split, solutions):
    if not values:
        if split[1] and patric_sum(split[0]) == patric_sum(split[1]):
            solutions.add(sean_sum(split[0]))

        return

    find_solutions(values[1:], [split[0] + [values[0], ], split[1]], solutions)
    find_solutions(values[1:], [split[0], split[1] + [values[0],]], solutions)

def solve(values):
    solutions = set()
    find_solutions(values, [[], []], solutions)

    if solutions:
        return max(solutions)
    else:
        return "NO"

with open(sys.argv[1]) as input_file:
    cases = int(input_file.readline())

    for case in xrange(1, cases + 1):
        candies = input_file.readline()
        values = [int(f) for f in input_file.readline().split()]

        answer = solve(values)
        
        print "Case #%d: %s" % (case, str(answer))

# vim: ts=4:sw=4:expandtab
