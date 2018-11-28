#!/usr/bin/python

import sys
import functools
import operator
import bisect

def isC(c):
    return c not in "aeiou"

def findNext(s, i, n):
    a = 0
    l = len(s)
    start = -1
    current = i
    while (a < n and current < l):
        if isC(s[current]):
            if start == -1:
                start = current
            a += 1
        else:
            start = -1
            a = 0
            
        current += 1

    if a < n:
        return -1
    else:
        return start

def solve(s, n):
    num = 0
    a = -1
    i = findNext(s,0,n)

    while (i != -1):
        r = i - (a+1)
        q = len(s) - (i + n)
        num += 1 + r + q + r*q

        a = i
        i = findNext(s, a+1, n)

    return num

    
    
    

def main():
    N = int(sys.stdin.readline()) # number of testcases
    for i in range(N):
        [s, n] = sys.stdin.readline().rstrip().split()
        n = int(n)
        result = solve(s, n)
        print ("Case #%s: %s" % (i+1, result))


if __name__ == '__main__':
    main()
