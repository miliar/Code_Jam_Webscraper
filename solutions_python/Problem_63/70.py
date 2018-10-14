#!/usr/bin/env python

import sys

def solve(L, P, C):
    count = 0
    t = L
    while t * C < P:
        count += 1
        t *= C

    result = 0
    while count > 0:
        if count %2 == 0:
            count /= 2
        else:
            count = (count - 1) / 2
        result += 1
            
    return result

def main():
    num = int(sys.stdin.readline().strip())
    for i in range(num):
        (L, P, C) = sys.stdin.readline().strip().split()
        result = solve(int(L), int(P), int(C))
        print "Case #%d: %d" % (i+1, result)

if __name__ == '__main__':
    main()
