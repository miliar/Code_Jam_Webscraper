# coding: utf-8 
from __future__ import division
import itertools
import math
#import numpy

def read_word(f):
	return next(f).strip()

def read_int(f, b=10):
	return int(read_word(f), b)

def read_letters(f):
	return list(read_word(f))

def read_digits(f, b=10):
	return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
	return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]
 
def read_arr(f, R, reader=read_ints, *args, **kwargs):
    res = []
    for i in range(R):
        res.append(reader(f, *args, **kwargs))
    return res
 
def solve(solver, fn, out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(T):
                case = read_case(fi)
                if i != T-1:
                    blank = read_word(fi)
                res = solver(case)
                write_case(fo, i+1, res)
 
################################################################################
 
def read_case(f):
    Cs = []
    for i in range(4):
        Rows = read_letters(f)
        Cs.append(Rows)
    return (Cs)
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq

def check_rows(case):
    for i in range(4):
        Win = case[i][0]
        if Win == '.':
            continue
        for j in range(4):
            if Win == '.':
                Win = None
                break
            if Win == 'T':
                Win = case[i][j]            
            if case[i][j] == Win or case[i][j] == 'T':
                continue
            else:
                Win = None
                break

        if Win != None:
            return Win

    return None

def check_cols(case):
    for i in range(4):
        Win = case[0][i]
        if Win == '.':
            continue

        for j in range(4):
            if Win == '.':
                Win = None
                break
            if Win == 'T':
                Win = case[j][i]
            if case[j][i] == Win or case[j][i] == 'T':
                continue
            else:
                Win = None
                break

        if Win != None:
            return Win

    return None

def check_diag(case):
    #print "Check diag"
    Win = case[0][0]
    for i in range(4):
        if case[i][i] == '.':
            Win = None
            break
        if case[i][i] == Win or case[i][i] == 'T':
            continue
        else:
            Win = None
            break
    if Win != None:
        return Win

    Win = case[0][3]
    for j in range(4):
        if case[j][3-j] == '.':
            Win = None
            break
        if case[j][3-j] == Win or case[j][3-j] == 'T':
            continue
        else:
            Win = None
            break
    #print Win
    if Win != None:
        return Win

    return None

def check_draw(case):
    Draw = True
    for i in range(4):
        for j in range(4):
            if case[i][j] == '.':
                Draw = False
                return Draw
    return Draw


 
def solve_small(case):
    Cs = case
    print Cs

    Win = check_rows(case)

    if Win != None:
        return str(Win) + " won"

    Win = check_cols(case)

    if Win != None:
        return str(Win) + " won"

    Win = check_diag(case)

    if Win != None:
        return str(Win) + " won"

    #print "Check Draw:"
    Draw = check_draw(case)
    if Draw is True:
        return "Draw"

    return "Game has not completed"

solve_large = solve_small

solve(solve_small, "TicTacToe")
