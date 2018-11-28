#!/usr/bin/python

import sys

#debug_on = True
debug_on = False

if (len(sys.argv) > 2):
    input_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')

else:
    print "Input and output files not specified"
    sys.exit(1)

num_cases = int(input_file.readline().strip())

def pdebug(line):
    if debug_on:
        print line

def poutput(line):
    print line
    output_file.write("%s\n" % line)

for i in (range(1, num_cases + 1)):
#for i in (range(1, 3)):

    C, F, X = input_file.readline().strip().split(" ")
    C = float(C)
    F = float(F)
    X = float(X)

    pdebug("C: %s" % C)
    pdebug("F: %s" % F)
    pdebug("X: %s" % X)

    d = 0
    r = 2

    #t = X / r
    #pdebug("Time: %s" % t)
    #old_t = t

    t = (X / r) + d
    old_t = t

    while 1:
        pdebug("r: %s" % r)
        pdebug("d: %f" % d)
        pdebug("t: %f" % t)
        if old_t < t:
            break

        d += (C / r)
        r += F
        old_t = t
        t = (X / r) + d

    poutput("Case #%s: %.7f" % (i, old_t))
