#!/usr/bin/env python

import sys

memo = {}

def helper(c, fn, f, x):
    if fn == 0:
        return x / 2.0

    if (c, fn, f, x) in memo:
        return memo[(c, fn, f, x)]
    
    a = helper(c, fn - 1, f, c) + x / (fn * f + 2.0)
    memo[(c, fn, f, x)] = a
    return a

def solve(c, f, x):
    
    ans = x / 2.0
    fnum = 1
    while True:
        a = helper(c, fnum, f, x)
        if a < ans:
            ans = a
            fnum += 1
            continue
        return ans
        

def main():
    lines = sys.stdin.readlines()
    test_num = int(lines.pop(0))

    for i in range(test_num):
        c,f,x = [float(n) for n in lines.pop(0)[:-1].split(' ')]
        print("Case #%d: %0.7f" % (i+1, solve(c,f,x)))

if __name__ == '__main__':
    main()

