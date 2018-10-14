#!/usr/bin/env python
# William Wu, 2013 April 13
# William.Wu@themathpath.com

import os, sys
import numpy as np
import math

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = False

# number of test cases
line = input_file.readline().strip()
T = int(line)

def palindromeQ(x):
    return (str(x) == str(x)[::-1])

# main method
def main():
    # process each case
    for t in xrange(0,T):
        # read case
        A, B = map(int, input_file.readline().strip().split())

        # a = ceil(sqrt(A))
        # b = floor(sqrt(B))
        a = int(math.ceil(math.sqrt(A)))
        b = int(math.floor(math.sqrt(B)))

        # initialization        
        count = 0

        # count how many numbers in [a,b] are palindromic and also whose squares are palindromic
        for u in xrange(a,b+1):            
            if not palindromeQ(u): # 1. determine if u is a palindrome
                continue
            else: # 2. determine if u^2 is a palindrome
                if palindromeQ(u*u):
                    count += 1

        # print report
        print "Case #%d: %s" % (t+1,count)

if __name__ == '__main__':
    main()