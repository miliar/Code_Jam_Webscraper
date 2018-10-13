#!/usr/bin/python

import sys

def solve(case):
    # Returns the number of unordered numbers
    c = map(int, case.split(' '))
    l = len(c)

    s = 0
    i = 0
    j = 1
    while i < l:
        if c[i] != j:
            s += 1
        i += 1
        j += 1
    return s

def main(data = "D-example.in"):
    f = open(data, 'r')
    inp = map(lambda x: x[:-1], f.readlines())

    T = int(inp[0])
    cases = inp[1:]

    i = 1
    j = 1
    while j < len(cases):
        print "Case #" + str(i) + ": %f" % solve(cases[j])
        j += 2
        i += 1

#main()
if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print sys.argv[0] + " <input file>"
