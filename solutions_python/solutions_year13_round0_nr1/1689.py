#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 13 Apr 2013

@author: Artem
'''
from __future__ import division
import os
import sys
import time


def write_case(f_out, out, k):
    out = "Case #%d: %s\n" % (k, out)
    f_out.write(out)
    #print out

def check(line):
    O = False
    X = False
    p = False
    
    line = list(set(line))
    if 'T' in line:
        line.remove('T')
    
    if '.' in line:
        p = True
        return (X, O, p) 
    
    if len(line) == 1:
        if line[0] == 'O':
            O = True
        elif line[0] == 'X':
            X = True
    return (X, O, p)

def solve(f_in, f_out):
    N = f_in.readline()
    if not N:
        print 'The input file is empty!'
        sys.exit()
    N = int(N)
    
    
    for k in xrange(1, N+1):
        board = []
        for _ in xrange(4):
            board.append(f_in.readline()[:-1:])
        _ = f_in.readline()
        #for b in board:
        #    print b

        O = False
        X = False
        p = False
        
        diag_r = [board[0][0], board[1][1], board[2][2], board[3][3]]
        diag_l = [board[0][3], board[1][2], board[2][1], board[3][0]]
        
        ans = check(diag_r)
        if ans[0]: X = True
        if ans[1]: O = True
        if ans[2]: p = True
        
        ans = check(diag_l)
        if ans[0]: X = True
        if ans[1]: O = True
        if ans[2]: p = True
        
        for line in board:
            line = [s for s in line]
            ans = check(line)
            if ans[0]: X = True
            if ans[1]: O = True
            if ans[2]: p = True
            
        for i in xrange(4):
            line = [board[0][i], board[1][i], board[2][i], board[3][i]]
            ans = check(line)
            if ans[0]: X = True
            if ans[1]: O = True
            if ans[2]: p = True
            
        if not p:
            if X and O:
                out = 'Draw'
            elif not X and not O:
                out = 'Draw'
            elif X:
                out = 'X won'
            elif O:
                out = 'O won'
        else:
            if not X and not O:
                out = 'Game has not completed'
            elif X and O:
                out = 'Draw'
            elif X:
                out = 'X won'
            elif O:
                out = 'O won'
        write_case(f_out, out, k)

def main():
    START = time.time()
    my_dir = os.getcwd()
    name = os.path.basename(__file__)[:-3:]
    
    file_in = "%s\\input\\%s.in" % (my_dir, name)
    file_out = "%s\\output\\%s.out" % (my_dir, name)
    with open(file_in, 'a+') as f_in:
        with open(file_out, 'w') as f_out:
            solve(f_in, f_out)
    
    print 'All done in %f s' % (time.time()-START)
    
if __name__ == '__main__':
    main()