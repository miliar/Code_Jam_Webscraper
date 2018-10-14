#!/usr/bin/python
#
# C-fairandsquare.py
#
# Sajjan Singh Mehta
# April 12, 2013

import numpy as np
import sys


isPalindrome = lambda x : x == x[::-1]

def square_palindrome_generator():
    n = 0
    d = 1
    
    while True:
        n += d
        d += 2
        
        if isPalindrome(str(n)):
            yield n

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    N = 1e14
    
    gen = square_palindrome_generator()
    squares = [0]
    
    while squares[-1] < N:
        squares.append(next(gen))
    
    sqrts = map(int, np.sqrt(squares))
    fairnsquares = np.array([squares[i] for i in xrange(len(squares)) if isPalindrome(str(sqrts[i]))])
    
    for i in xrange(1, T + 1):
        A, B = map(int, sys.stdin.readline().split())
        print 'Case #%d:' % i, sum(map(int, (fairnsquares >= A) & (fairnsquares <= B)))
    

