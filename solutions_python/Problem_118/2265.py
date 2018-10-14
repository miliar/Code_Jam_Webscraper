#!/usr/bin/env python

def is_palin(val):
    return str(val) == str(val)[::-1]

def process(A, B):
    from math import sqrt, ceil, floor
    start, end = int(ceil(sqrt(float(A)))), int(floor(sqrt(float(B))))
    cnt = 0
    for i in range(start, end+1):
        if is_palin(i) and is_palin(i*i): cnt += 1
    return cnt

if __name__ == "__main__":
    import sys
    from string import strip, split
    line = strip(sys.stdin.readline())
    size = int(line)
    for test in range(1, size+1):
        print "Case #%d:" %(test),
        line = strip(sys.stdin.readline())
        [A, B] = split(line)
        print process(A, B)
