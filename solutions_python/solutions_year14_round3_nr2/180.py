from _heapq import heappop
from collections import deque
from copy import copy
import math
import itertools
import numpy as NP


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


def solve(fn, out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            case_number = read_int(fi)
            for i in range(1, case_number + 1):
                case = read_case(fi)
                res = solve_case(case)
                write_case(fo, i, res)

################################################################################


def read_case(f):
    f.next()
    return read_words(f)


def write_case(f, i, res):
    f.write('Case #%d: ' % i)
    f.write(str(res))
    f.write('\n')
    print 'Case #%d: %s' % (i, str(res))

################################################################################

def simplify(string):
    string = list(string)
    for i in xrange(len(string)-1,0,-1):
        if string[i-1] == string[i]:
           del string[i]
    return string

def solve_case(case):
    trains = map(lambda l: simplify(l), case)
    pos = 0
    for perm in itertools.permutations(trains):
        geweest = set([])
        possible = True
        for i in xrange(len(perm)):
            for j in xrange(len(perm[i])):
                cur = perm[i][j]
                if cur in geweest:
                    if prev != cur:
                        possible = False
                        break
                prev = cur
                geweest.add(cur)
            if not possible:
                break
        else:
             pos+=1
    return pos

DEBUG = 'f'
solve("btest")