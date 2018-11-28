#! /usr/bin/env python

import sys
from math import sqrt


def isPalindrome(x):
    
    rx = int(str(x)[::-1])
    return x == rx


def isPerfectSquareOfPalindrome(x):
   
    i = 0

    while (i * i) < x:
        i += 1
    
    return (i * i == x) and isPalindrome(i)


def squareAndFair(a, b):

    predicate = lambda x: isPalindrome(x) and isPerfectSquareOfPalindrome(x)
    return filter(predicate, range(a, b+1))


def main():

    f_in  = open(sys.argv[1], 'r')
    f_out = open(sys.argv[2], 'w')

    T = int(f_in.readline())

    for case_number in range(1, T+1):

        A, B = f_in.readline().split()
        A = int(A)
        B = int(B)
        result = len(squareAndFair(A,B))
        f_out.write("Case #{}: {}\n".format(case_number, result))

    f_in.close()
    f_out.close()



if __name__ == "__main__":
    main()
