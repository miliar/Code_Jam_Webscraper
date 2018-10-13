#! /usr/bin/env python

## Written by Joey Tuong- deuterium.ion@gmail.com
## Created on 09:22 Saturday April 14 2012
## dance.py - dancing with the googlers
## Produced for Google Code Jam 2012
## All rights reserved.


import sys


def main(input):
    num_cases = int(input.pop(0))
    for case in range(1, num_cases + 1):
        data = [int(i) for i in input[case-1].split()]
        num_googlers = data.pop(0)
        surprising = data.pop(0)
        best = data.pop(0)
        
        badcases = []
        scases = []
        gcases = []
        # Cases that must be surprising
        for i in range(len(data)):
            c = data[i]
            if (c > 2 and c < 3*best - 4) or (c <= 2 and best > c):
                badcases.append(i)
            elif c < 3*best - 2:
                scases.append(i)
            else:
                gcases.append(i)
        answer = len(scases[:surprising] + gcases)
        
        print "Case #%d: %s" % (case, answer)


try:
    data = open(sys.argv[1]).read().split("\n")
except IOError:
    print "Invalid input file."
except IndexError:
    while True:
        num_statements = int(raw_input("Lines: "))
        args = ["1"]
        for i in range(num_statements):
            args.append(raw_input())
        print "Output:"
        main(args)
else:
    if len(sys.argv) > 2:
        outfile = sys.argv[2]
    else:
        outfile = ".".join(sys.argv[1].split(".")[:-1])+".out"

    sys.stdout = open(outfile, "w")
    main(data)
    sys.stdout.close()
