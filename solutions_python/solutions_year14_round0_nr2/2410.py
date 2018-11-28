#!/usr/bin/env python
import fileinput

def solve(C, F, X, c=2.0):
    res = 0.0
    while X/c > C/c + X/(F+c):
        res += C/c
        c += F
    return res + X/c

def main():
    inp = fileinput.input()

    T = int(inp.next())

    for i in xrange(T):
        C, F, X = [float(x) for x in inp.next().split(" ")]
        print "Case #%d: %.7f" % (i+1, solve(C, F, X))

if __name__ == '__main__':
    main()