""" 
Code Jam 2013
Problem: Fair and Square
Usages: 
  $ python script < input > output
  PS > gc input | python script | sc output.
"""

import sys, math

def fscount(l, u):
    c = 0
    for s in psquares(l, u):
        if is_palindrome(s):
            c += 1
    return c

def fs(l, u):
    return [s for s in psquares(l, u) if is_palindrome(s)]

def fscount2(l, u, allfs):
    c = 0
    for fs in allfs:
        if l <= fs <= u:
            c += 1
        if fs > u:
            return c
    return c

def psquares(l, u):
    root_min = int(math.ceil(math.sqrt(float(l))))
    root_max = int(math.floor(math.sqrt(float(u))))
    for r in range(root_min, root_max+1):
        if is_palindrome(r):
            yield r**2

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    allfs = fs(1, 10**14)
    numcases = int(sys.stdin.readline().strip())
    for i in range(1, numcases+1):
        l, u = map(int, sys.stdin.readline().strip().split())
        result = fscount2(l, u, allfs)
        print "Case #%d: %s" % (i, result)
