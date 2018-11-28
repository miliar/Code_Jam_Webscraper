#!/usr/bin/env python

from math import sqrt

def isPalindrome(N):
    s = str(N)
    for i in range(1+(len(s)/2)):
        if s[i]!=s[-i-1]:
            return False
    return True

def isFair(N):
    if not isPalindrome(N):
        return False
    
    n = int(sqrt(N))
    if not n*n==N:
        return False
    return isPalindrome(n)

if __name__ == '__main__':
    z = raw_input()
    for i in range(1, int(z)+1):
        A, B = map(int, raw_input().split())
        print 'Case #%d: %s' % (i, len(filter(isFair, range(A,B+1))))
    pass

