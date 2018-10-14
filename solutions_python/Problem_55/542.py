#!/usr/bin/env python

"""Google Code Jam 2010, Qualification Round, C."""

__author__ = "Samuel Spiza"

import sys
import math

#FILE_NAME = "C-practice.in"
FILE_NAME = "C-small-attempt0.in"
#FILE_NAME = "C-large.in"

def main():
    inputFile = open(FILE_NAME, "r")
    N, cases = getCases(inputFile.readlines())
    inputFile.close()
    
    results = [do(case) for case in cases]

    string = "\n".join(["Case #%s: %s" % (z+1, results[z]) for z in range(N)])
    
    print string
    file = open(FILE_NAME.rsplit(".", 1)[0] + ".out", "w")
    file.write(string.strip())
    file.close()

    return 0

def getCases(lines):
    N = int(lines[0].strip())
    i = 0
    cases = []
    for line in lines[1:]:
        if i == 0:
            cases.append([int(x) for x in line.strip().split()][:2])
        else:
            cases[-1].append([int(x) for x in line.strip().split()])
        i = (i + 1)%2
    return N, cases

def do(case):
    s = 0
    for i in range(case[0]):
        j = 1
        while j <= len(case[2]) and sum(case[2][:j]) <= case[1]:
            j += 1
        s += sum(case[2][:j - 1])
        case[2] = case[2][j - 1:] + case[2][:j - 1]
    return s

    
if __name__ == "__main__":
    sys.exit(main())
