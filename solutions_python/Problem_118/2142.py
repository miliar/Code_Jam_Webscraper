#!/usr/bin/python

import getopt
import sys

import re
import string

from math import sqrt

from pprint import pprint as pp

"""
from https://code.google.com/codejam/contest/351101/dashboard#s=p1

"""

filename = ''

tcs = []

########################
# inputtc
#
# absorbs three lines of text file f
#
# returns a dict of parsed test case data
#
def inputtc(f):
    # absorb test case data starting at lineindex
    d = {}
    toks = f.readline().split()
    d['min'] = int(toks[0])
    d['max'] = int(toks[1])
    
    return d

########################
# input
#
# setup the test case run
#
# - open and parse file
# - acquire number of test cases
# - generate test case dict list
#
# returns number of test cases to run
# 
def input():
    f = open(filename, "r")
    
    num_tcs = int(f.readline().split()[0])
    #num_tcs = int(f.readline().split()[0])
    
    for i in range(num_tcs):
        tcs.append(inputtc(f))
    
    return num_tcs
    
########################
def is_palindrome(i):
    return str(i) == str(i)[::-1]

########################
# run_test
#
# takes 0-based test case index, tci
def run_test(tci):
    
    results = []
    
    minfns = tcs[tci]['min']
    maxfns = tcs[tci]['max']
    
    min = int(sqrt(minfns))
    max = int(sqrt(maxfns))+1
    
    check = [ x**2 for x in range(min, max) ]
    
    n = 0
    
    for i in range(len(check)):
        if is_palindrome(check[i]) and \
           is_palindrome(int(sqrt(check[i]))) and \
           check[i] >= minfns and \
           check[i] <= maxfns:
            n += 1

    results.append(n)

    print "Case #%d: " % (tci + 1) + ' '.join([str(x) for x in results])
    
########################
def main():

    num_tcs = input()
    
    for tc in range(num_tcs):
        run_test(tc)

########################
if __name__ == "__main__":
    
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)

    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)

    # process arguments
    try:
        filename += args[0]
    except:
        print "Provide a file for analysis"

    main()
    
