#!/usr/bin/env python

"""Google Code Jam 2010, Round 1C, A."""

__author__ = "Samuel Spiza"

import sys
import math

#FILE_NAME = "A-practice.in"
#FILE_NAME = "A-small-attempt0.in"
FILE_NAME = "A-large.in"

cnt = 0

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
            i = int(line.strip())
            cases.append([])
        else:
            cases[-1].append([int(x) for x in line.strip().split()])
            i -= 1
    return N, cases

def do(case):
    cnt = 0
    z = []
    for a in case:
        for b in z[:]:
            if (a[0]-b[0])*(a[1]-b[1]) < 0:
                cnt += 1
        z.append(a)
    return cnt

if __name__ == "__main__":
    sys.exit(main())
