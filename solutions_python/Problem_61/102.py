#!/usr/bin/env python

"""Google Code Jam 2010, Round 1B, C."""

__author__ = "Samuel Spiza"

import sys
import math

#FILE_NAME = "C-practice.in"
FILE_NAME = "C-small-attempt1.in"
#FILE_NAME = "C-large.in"

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
    cases = []
    for line in lines[1:]:
        cases.append(int(line.strip()))
    return N, cases

def do(case):
    n = case
    s = 0
    for i in range(1, n):
        s += func(i, n)
    return s%100003

def func(i, n):
    if i < 1:
        return 0
    elif n <= i:
        return 0
    elif i == 1:
        return 1
    elif n == i + 1:
        return 1
    x = 0
    for j in range(2*i - n, i):
        t = func(j, i)
        if 0 < t:
            p = n - i - 1
            q = i - j - 1
            a = math.factorial(q)
            b = math.factorial(p)
            c = math.factorial(p-q)
            y = b/(a*c)
            x += t*y
    return x
    
def cnt(i, tree):
    if len(tree) == 0:
        return i
    else:
        for key in tree:
            i = cnt(i + 1, tree[key])
    return i

if __name__ == "__main__":
    sys.exit(main())
