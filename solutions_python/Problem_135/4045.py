#!/usr/bin/python

import getopt
import sys

import re
import string

from pprint import pprint as pp

"""
from https://code.google.com/codejam/contest/2974486/dashboard#s=p2

"""

filename = ''

tcs = []

########################
# inputtc
#
# absorbs lines of text file f
#
# returns a dict of parsed test case data
#
def inputtc(f):
    # absorb test case data starting at lineindex
    d = {}
    toks = f.readline().split()
    d['R1'] = int(toks[0])
    
    d['M1'] = []
    for i in xrange(4):
        toks = f.readline().split()
        d['M1'].append(toks)

    toks = f.readline().split()
    d['R2'] = int(toks[0])

    d['M2'] = []
    for i in xrange(4):
        toks = f.readline().split()
        d['M2'].append(toks)
    
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
# run_test
#
# takes 0-based test case index, tci
def run_test(tci):
    
    results = ""
    #print tci
    
    # if there is a unique number in R1 of M1 and R2 of M2
    # we're golden
    #
    # if there is more than 1, Bad magician
    #
    # if there is 0, Cheater
    
    r1 = tcs[tci]['R1']-1
    r2 = tcs[tci]['R2']-1
    map1 = tcs[tci]['M1']
    map2 = tcs[tci]['M2']
    
    matches = []
    for i in map2[r2]:
        if i in map1[r1]:
            matches.append(i)
   
    if len(matches) == 0:
        results = 'Volunteer cheated!'
    elif len(matches) == 1:
        results = str(matches[0])
    else:
        results = 'Bad magician!'

    print "Case #%d: %s" % ((tci + 1), str(results))
    
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
    
