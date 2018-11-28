# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
#import numpy as np
# import scipy as sc
# import itertools
import sys


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
    return [reader(f, *args, **                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         kwargs) for i in range(R)]


def main_reader(T, f):
    N, K = read_ints(f)
    return {'T': T, 'N': N, 'K':K}

def enumeration_solver(T, N=None, K=None):
    """
    Construct the stalls allocation sequence
    """
    spans = [N]
    while K>0:
    #    print('People {} Spans: {}'.format(K,'X'.join(['*'*int(t) for t in spans])))
        mspan = spans[-1]
        if mspan%2==0:
            p = int(mspan/2)-1
        else:
            p = int((mspan-1)/2)

        spans.pop()
        ls = p
        rs = (mspan-1)-p
        if p>0:
            spans.append(p)
        if p<(mspan-1):
            spans.append(mspan-1-p)
        spans.sort()
        K-=1
    #print('People {} Spans: {}'.format(K, 'X'.join(['*' * int(t) for t in spans])))
    return 'Case #{}: {} {}\n'.format(T,max([ls,rs]),min([ls,rs]))


if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '.out'

    try:
        with open(input_file, 'r') as f:
            T = read_int(f)  # Number of test cases
            for t in range(1, T + 1):
                sys.stdout.write(enumeration_solver(**main_reader(t, f)))
    except IOError:
        print('File %s not found' % input_file)
        exit(1)
