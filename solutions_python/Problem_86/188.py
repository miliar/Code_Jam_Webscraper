#!/usr/bin/env python
import sys

def solve(min, max, list):
    result = []
    factor = reduce(lambda a,b: lcm(a,b), list)
    for i in xrange(min, max+1):
        if mod1(factor,i) == 0:
            sum = 0
            for val in list:
                sum += mod1(val, i)
            if sum == 0:
                return i
    return 'NO'

def mod1(x,y):
    if x>=y:
        return x%y
    else:
        return y%x

def lcm(a,b):
    return (a*b)/gcd(a,b)

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    infile = open('C-small-attempt0.in', 'rU')
    outfile = open('out', 'w')
    inputs = int(infile.readline())
    for i in xrange(0,inputs):
        matrix = []
        rows = infile.readline().split()
        min = int(rows[1])
        max = int(rows[2])
        list = infile.readline().split()
        list = map(lambda x: int(x), list)
        result = solve(min, max, list)
        outfile.write(("Case #%d: %s\n") % (int(i+1), str(result)))
    infile.close()
    outfile.close()
