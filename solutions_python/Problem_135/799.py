#!/usr/bin/env pypy
import sys, os

outfile = open("%s.out" % sys.argv[1], "w")
case_number = 1

def solving(case):
    global case_number
    possible1 = set(case[0][1][case[0][0] - 1])
    possible2 = set(case[1][1][case[1][0] - 1])
    r = possible1 & possible2
    if len(r) == 1:
        result = list(r)[0]
    elif len(r) == 0:
        result = "Volunteer cheated!"
    else:
        result = "Bad magician!"
    outfile.write("Case #%d: %s\n" % (case_number, result))
    case_number += 1

with open(sys.argv[1]) as infile:
    case = []
    for l in infile.readlines()[1:]:
        l = l.replace('\n', '')
        if len(l) == 1:
            if len(case) == 2:
                solving(case)
                case = []
            case.append([int(l), []])
        else:
            case[-1][-1].append(l.split())
    solving(case)
    
outfile.close()
