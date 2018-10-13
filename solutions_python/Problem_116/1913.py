#!/usr/bin/python

import getopt
import sys

import re
import string

from pprint import pprint as pp

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
    board = []
    for i in range(4):
        board.append(f.readline())
    d['board'] = board
    #drop empty line
    f.readline()
    
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
def check(a, board, flip):
    diag = ''.join([board[i][i].replace('T', a) for i in range(4)])
    diag2 = ''.join([board[3-i][i].replace('T', a) for i in range(4)])
    return a*4 in ''.join(board).replace('T', a) or \
        a*4 in ''.join(flip).replace('T', a) or \
        a*4 in diag or \
        a*4 in diag2
    
########################
# run_test
#
# takes 0-based test case index, tci
def run_test(tci):
    
    results = []

    board = tcs[tci]['board']

    #flip = [ ''.join(['.' for i in range(4)]) + '\n' for i in range(4)]
    flip= []
    for i in range(4):
        line = ''
        for j in range(4):
            line = line + board[j][i]
        flip.append(line + '\n')
            
    #check X
    x_won = check('X', board, flip)

    #check 0
    o_won = check('O', board, flip)
    
    full = not '.' in ''.join(board)
        
    if not x_won and not o_won and full:
        results = 'Draw'
    elif x_won:
        results = 'X won'
    elif o_won:
        results = 'O won'
    else:
        results = 'Game has not completed'
        

    print "Case #%d: %s" % (tci + 1, results)
    
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
    
