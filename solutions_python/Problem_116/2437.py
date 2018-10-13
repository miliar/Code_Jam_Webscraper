#!/usr/bin/env python
# William Wu, 2013 April 13
# William.Wu@themathpath.com

import os, sys
import numpy as np

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = False

# number of test cases
line = input_file.readline().strip()
T = int(line)

# for anti_trace
i=np.arange(4)
j=i[::-1]

# status code --> status string
def status_string(code):
    if 1==code:
        return "X won"
    elif 2==code:
        return "O won"
    elif 3==code:
        return "Draw"
    elif 4==code:
        return "Game has not completed"

# map X or T to 1, and others to 0
def char_to_num_X(c):
    if 'X'==c or 'T'==c:
        return 1
    else:
        return 0

# map O or T to 1, and others to 0
def char_to_num_O(c):
    if 'O'==c or 'T'==c:
        return 1
    else:
        return 0

# determine if numerical board is a winner for one side
def winQ(mat):
    column_sums = mat.sum(axis=0)
    row_sums = mat.sum(axis=1)
    trace = mat.trace(offset=0)
    anti_trace = mat[i,j].sum(axis=0)
    if 4 in column_sums or 4 in row_sums or 4==trace or 4==anti_trace:
        return True
    else:
        return False

# main method
def main():
    # preallocation
    X_mat = np.zeros((4,4))
    O_mat = np.zeros((4,4))

    # process each case
    for t in xrange(0,T):
        # read board
        empty_spaces_flag = False
        for u in xrange(0,4):
            chars = list(input_file.readline().strip())
            if '.' in chars: empty_spaces_flag = True
            X_mat[u,:] = map(char_to_num_X,chars)
            O_mat[u,:] = map(char_to_num_O,chars)
            if debug_flag: print chars

        if debug_flag: print X_mat
        if debug_flag: print O_mat

        # analyze board
        status_code = 0
        if winQ(X_mat):
            status_code = 1
        elif winQ(O_mat):
            status_code = 2
        else:
            if empty_spaces_flag:
                status_code = 4    
            else:
                status_code = 3

        # print report
        print "Case #%d: %s" % (t+1,status_string(status_code))

        # consume empty line
        input_file.readline()

if __name__ == '__main__':
    main()