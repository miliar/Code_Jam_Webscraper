#!/usr/bin/env python2.7

from sys import stdin
from math import sqrt, ceil

def isPalindrome(n):
    s = str(n); return s == s[::-1]

# based on http://www.ardendertat.com/2011/12/01/programming-interview-questions-19-find-next-palindrome-number/
def getNextPalindrome(n):
    while True:
        s = str(n); l = len(s); half = l/2
        left, middle = s[:half], s[l/2] if l%2 else ''
        newN = int(left + middle + left[::-1])
        if newN > n: return newN
        if s[(l-1)/2] == '9':
            increment = 10 ** ((half)+1)
            n = ((n/increment)+1)*increment
            continue
        else:
            increment = 10 ** (half)
            if middle == '': increment *= 1.1
            return newN + int(increment)

def getStatus(a, b):
    count = 0
    ra = int(ceil(sqrt(a)))
    rb = int(sqrt(b))
    if isPalindrome(ra): n = ra
    else: n = getNextPalindrome(ra)
    while n <= rb:
        if isPalindrome(n*n): count += 1; # print n
        n = getNextPalindrome(n)
    return count

numcases = int(stdin.readline().strip())
for casenum in xrange(numcases):
    line = stdin.readline().strip()
    try: status = getStatus(*map(int, line.split(' ')))
    except: print 'LINE', line; raise
    print "Case #%d: %s" % (casenum+1, status)
