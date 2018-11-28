#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import sys

def main():
    if len(sys.argv) != 2:
        print "Usage: %s [FILE]\n" % (sys.argv[0])
        exit()

    with open(sys.argv[1]) as input_file:
        t = int(input_file.readline())
        for case, line in enumerate(input_file, 1):
            print "Case #%d:" % (case),

            tmp = line.split()
            n = int(tmp[0])

            jpoints = [float(s) for s in tmp[1:]]
            sum_jpoints = sum(jpoints)

            # exclude safe constestants
            apoints = []
            for p1 in jpoints:
                if sum([p1 - p2 + 1 for p2 in jpoints if p2 < p1]) > sum_jpoints:
                    apoints.append(0.000000)
                else:
                    apoints.append(None)

            # find all non-safe points
            nonsafe = [jpoints[i] for i, ap in enumerate(apoints) if ap == None]

            maxp = max(nonsafe)
            apoints_per_nonsafe = (sum_jpoints - sum([maxp - x for x in nonsafe])) / len(nonsafe)

            for p, ap in zip(jpoints, apoints):
                if ap != None:
                    print "0.000000",
                else:
                    print ((maxp - p) + apoints_per_nonsafe) * 100 / sum_jpoints,

            # end of case
            print

main()

