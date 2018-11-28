#!/usr/bin/env python

import sys
import itertools
import math

def open_input(file):
    try:
        f = open(file, "r")
        return f
    except:
        print "can not open ", file
        sys.exit(1)

palindromes = {}
def is_palindrome(num):
    if num in palindromes:
        return True

    s = str(num)
    r = s[::-1]
    if s == r:
        palindromes[num] = True
        return True
    else:
        return False

def do_solve(start, end):
    num = start
    count = 0
    while (num <= end):
        if is_palindrome(num):
            sq = math.sqrt(num)
            if sq == math.floor(sq):
                if (is_palindrome(int(sq))):
                    count += 1
        num += 1
    return count

def solve(input):
    """ T = # test case """
    T = int(input.readline())

    for i in range(T):
        line = input.readline().rstrip()
        start, end = line.rsplit(' ')
        print "Case #{0}: {1}".format(i+1,
                do_solve(int(start), int(end)))

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(open_input(sys.argv[1]))
    else:
        print 'require input'
        sys.exit(1)
