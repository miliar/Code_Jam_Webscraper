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

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]
 
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
                res = solver(case)
                write_case(fo, i+1, res)
 
def read_case(f):
    (L, X) = read_ints(f)
    P = read_letters(f)
    print (L, X, P)
    return (L, X, P)
 
def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')
 
################################################################################

INF = float('inf')
 
import heapq

def multiply(row, column):
    mul_dict = { ('1', '1') : '1'
                , ('1', 'i') : 'i'
                , ('1', 'j') : 'j'
                , ('1', 'k') : 'k'
                , ('i', '1') : 'i'
                , ('i', 'i') : '-1'
                , ('i', 'j') : 'k'
                , ('i', 'k') : '-j'
                , ('j', '1') : 'j'
                , ('j', 'i') : '-k'
                , ('j', 'j') : '-1'
                , ('j', 'k') : 'i'
                , ('k', '1') : 'k'
                , ('k', 'i') : 'j'
                , ('k', 'j') : '-i'
                , ('k', 'k') : '-1'
                , ('-1', '1') : '-1'
                , ('-1', 'i') : '-i'
                , ('-1', 'j') : '-j'
                , ('-1', 'k') : '-k'
                , ('-i', '1') : '-i'
                , ('-i', 'i') : '1'
                , ('-i', 'j') : '-k'
                , ('-i', 'k') : 'j'
                , ('-j', '1') : '-j'
                , ('-j', 'i') : 'k'
                , ('-j', 'j') : '1'
                , ('-j', 'k') : '-i'
                , ('-k', '1') : '-k'
                , ('-k', 'i') : '-j'
                , ('-k', 'j') : 'i'
                , ('-k', 'k') : '1'
                }
    #print mul_dict[(row, column)]
    return mul_dict[(row, column)]

def found(stream, symbol):

    if not stream:
        return False

    RepeatP = list(stream)
    print (RepeatP, symbol)
    NowC = '1'
    for i in range(len(RepeatP)):
        NowC = multiply(NowC, RepeatP[i])
        if symbol == 'i':
            if NowC == symbol:
                return (found(RepeatP[i+1:], 'j') or found(RepeatP[i+1:].insert(0, symbol), 'i'))
        elif symbol == 'j':
            if NowC == symbol:
                return (found(RepeatP[i+1:], 'k') or found(RepeatP[i+1:].insert(0, symbol), 'j'))
        elif symbol == 'k':
            if NowC == symbol and (i + 1) == len(RepeatP):
                return True

    return False

    
 
def solve_small(case):
    (L, X, P) = case
    Total = L * X
    RepeatP = list(P)
    for i in range(1, X):
        RepeatP += list(P)

    #multiply('i', 'j')
    #print RepeatP
    res = found(RepeatP, 'i')
    if res:
        return 'YES'
    else:
        return 'NO'

solve_large = solve_small

#def solve_large(case):
    

#    return res




solve(solve_small, "Dijkstra")
