#! /usr/bin/python

import sys

def solve(a, b, k):
    result = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                result += 1
    return result

def main():
    fh = open(sys.argv[1])
    for i in range(int(fh.readline())):
        (a, b, k) = [int(x) for x in fh.readline().split()]
        print "Case #%d: %s" % (i + 1, solve(a, b, k))

main()
