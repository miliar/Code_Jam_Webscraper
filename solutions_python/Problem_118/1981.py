#!/usr/bin/python

import sys
import math
import itertools

def is_palindrome(nn):
    n=str(nn)
    return n[:int(math.floor(float(len(n)/2)))] == n[:int(math.ceil(float(len(n))/2))-1:-1]

def is_square(n):
    return math.sqrt(n).is_integer() 

def main():
    n_cases = int(sys.stdin.readline())
    for i in xrange(1,n_cases+1):
        result=0
        a,b = map(int, sys.stdin.readline().strip().split(' '))
        for n in xrange(a,b+1):
            if is_square(n):
                if is_palindrome(n):
                    if is_palindrome(int(math.sqrt(n))):
                        result += 1
        print 'Case #{0}: {1}'.format(i, result)

         

if __name__ == '__main__':
    main()
