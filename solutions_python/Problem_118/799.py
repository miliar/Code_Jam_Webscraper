#! /usr/bin/python

__author__ = 'Thomas "noio" van den Berg'

### IMPORTS ###
import sys
import numpy as np
# import gmpy
from pprint import pprint


def isqrt(n):
    """ Newtons algo from stackoverflow """
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

### FUNCTIONS ###    
def is_palindrome(number):
    s = str(number)
    i = 1
    for letter in s:
        if letter != s[-i]:
            return False
        i += 1
        if i > len(s) // 2:
            break
    return True


def do(A,B):
    palins = set()
    fairsquare = set()
    num = A
    while num <= B:
        if is_palindrome(num):
            palins.add(num)
            print num
            sq = isqrt(num)
            if sq * sq == num:
                if sq in palins or is_palindrome(sq):
                    fairsquare.add(num)
        num += 1

    print fairsquare 
    return len(fairsquare)



### PROCESS INPUT FILE ###

if __name__ == '__main__':
    f = open(sys.argv[1])
    fout = open(sys.argv[1].replace('.in','.out'),'w')

    T = int(f.readline())
    for case in xrange(T):
        A, B = [int(nm) for nm in f.readline().split()]

        ans = do(A, B)
        print ans
        fout.write('Case #%d: %s\n'%(case+1,ans))
