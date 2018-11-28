#!/usr/bin/env python

import sys


def magic(first_line, second_line):
    first_line = set(first_line)
    second_line = set(second_line)
    common = first_line & second_line
    if len(common) == 1:
        return list(common)[0]
    if len(common) == 0:
        return "Volunteer cheated!"
    if len(common) > 1:
        return "Bad magician!"

def getline(lines):
    n = int(lines[0].rstrip())
    line = lines[n].rstrip().split()
    return line

input = open(sys.argv[1]).readlines()
T = int(input[0])
input = input[1:]
for case in range(1, T+1):
    lines = input[:5]
    line1 = getline(lines)
    input = input[5:]
    lines = input[:5]
    line2 = getline(lines)
    input = input[5:]
    sys.stdout.write('Case #%s: %s\n' % (case, magic(line1, line2)))    
