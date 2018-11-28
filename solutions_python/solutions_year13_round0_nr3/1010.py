#!/usr/bin/python

""""Solve Problem B of the the Google Code Jam 2013 Qualification Round -
Lawnmower."""

import sys
import gmpy2


def my_range(start, stop):
   i = start
   while i < stop:
       yield i
       i += 1

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def fair_square_numbers_in_range(lower, upper):
    count = 0
    for i in my_range(lower, upper+1):
        #print i, int(gmpy2.is_square(i)), int(is_palindrome(i)), int(is_palindrome(int(round(gmpy2.sqrt(i)))))
        if gmpy2.is_square(i) and is_palindrome(i) and is_palindrome(int(round(gmpy2.sqrt(i)))):
            #print i
            count += 1
    return count

def main():
    numberOfCases = int(sys.stdin.readline().strip())
    for i in range(numberOfCases):
        lower, upper = sys.stdin.readline().strip().split(' ')
        lower = int(lower)
        upper = int(upper)
        print "Case #%i: %i"%(i+1, fair_square_numbers_in_range(lower, upper))


if __name__ == '__main__':
    main()