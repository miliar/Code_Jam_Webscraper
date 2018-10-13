#!/usr/bin/env python
import sys
import math

i = 0
t = 0
c = 0
n = 0
m = 0
x = 0
pals = set()

def is_palindrome(x):
    global pals
    if x in pals:
        return True
    strx = str(x)
    p = len(strx)
    for i in range(p // 2):
        if strx[i] != strx[p-1-i]:
            return False
    pals.add(x)
    return True

def calculate(a, b):
    fair = [x for x in range(a, b+1) if is_palindrome(x)]
    square = 0
    for f in fair:
        y = math.sqrt(f)
        (m, d) = math.modf(y)
        if m == 0.0:
            d = int(d)
            if is_palindrome(d):
                square += 1
    return square

def process(line):
    global t
    global i
    global c

    i += 1;

    if i == 1:
        t = int(line)
        c = 1
    else:
        (a, b) = [int(d) for d in line.split()]
        result = calculate(a, b)
        print "Case #{}: {}".format(c, result)
        c += 1



if len(sys.argv) < 2:
    print "Please supply the input file as argument"
    sys.exit(2)

filename = sys.argv[1]
with open(filename) as f:
    for line in f:
        if len(line.strip()):
            process(line.strip())
