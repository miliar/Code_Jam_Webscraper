#! /usr/bin/env python

## Written by Joey Tuong- deuterium.ion@gmail.com
## Created on 09:03 Saturday April 14 2012
## googlerese.py - 
## Produced for Google Code Jam 2012
## All rights reserved.


import sys


def main(input):
    num_cases = int(input.pop(0))
    translate = {'a': 'y', ' ': ' ', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', "q":"z"}
    for case in range(1, num_cases + 1):
        answer = ""
        for i in input[case-1]:
            if i in translate:
                answer += translate[i]
            else:
                answer += i    
        
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
