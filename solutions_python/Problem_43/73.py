#!/usr/bin/env python

import sys

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()
    
    N = int(lines[0])
    
    for n in range(N):
        solution = solve(lines[n+1].strip())
        print "Case #%d: %d" % (n+1, solution)

def solve(s):
    digits = {}
    numbers = [1,0] + range(2,100)
    idx = 0
    
    for c in s:
        if not digits.has_key(c):
            digits[c] = numbers[idx]
            idx += 1
    
    if idx == 1:
        idx = 2
    total = 0
    for c in s:
        total *= idx
        total += digits[c]
    
    return total

if __name__ == '__main__':
    main()