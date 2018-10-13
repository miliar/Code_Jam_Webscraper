#!/usr/bin/env python
import sys

squares = [1,4,9,121,484]

def main():
    N = int(sys.stdin.readline())
    for i in range(1, N+1):
        a, b = [int(x) for x in sys.stdin.readline().split(' ')]
        print "Case #%d: %d" % (i, len([x for x in squares if a <= x <= b]))

if __name__ == '__main__':
    main()