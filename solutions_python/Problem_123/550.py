#!/usr/bin/env python
import sys

l = 0
c = 0
a = 0
r = 0
n = 0

def is_solvable(a, m):
    sm = m[:]
    while len(sm) > 0:
        x = sm.pop(0)
        if x < a:
            a += x
        else:
            return False
    return True

def remove(a, m):
    nm = m[:-1]
    return nm

def add(a, m):
    for x in m:
        if x < a:
            a += x
        else:
            z = m[:]
            z.append(a-1)
            z.sort()
            return z
    return None

def solve(s, a, m):
    if s > 10:
        return s
    if is_solvable(a, m):
        return s
    else:
        first = solve(s+1, a, remove(a, m))
        #        second = first + 1
        if a > 1:
            second = solve(s+1, a, add(a, m))
        else:
            return first
        if first < second:
            return first
        else:
            return second

def calc():
    global a
    global m

    m.sort()
    result = solve(0, a, m)
    return result

def process(line):
    global l
    global c
    global t
    global a
    global m
    global n

    l += 1;

    if l == 1:
        c = 1
    else:
        if a == 0:
            (a, n) = [ int(d) for d in line.split() ]
        else:
            m = [ int(d) for d in line.split() ]
            result = calc()
            print "Case #{}: {}".format(c, result)
            c += 1
            a = 0


if len(sys.argv) < 2:
    print "Please supply the input file as argument"
    sys.exit(2)

filename = sys.argv[1]
with open(filename) as f:
    for line in f:
        if len(line.strip()):
            process(line.strip())

