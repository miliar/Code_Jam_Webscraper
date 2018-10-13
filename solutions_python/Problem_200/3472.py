# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
# import numpy as np
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
    N = read_int(f)
    return {'T': T, 'N': N}


def improved_enumeration_solver(T, N=None):
   """
   """
   n = N
   while n>0 :
       idx = inversion_idx(n)
       if idx is None:
           return 'Case #{}: {}\n'.format(T, n)
       else:
           num = str(n)
           leading = num[0:max([0,idx])]
           trailing = num[idx:]
           new_trailing=(int(trailing[0])-1)
           if new_trailing==-1:
               new_trailing = 9
           trailing = str(new_trailing) + '9'*(len(trailing)-1)
           #trailing[1:]='9'*(len(trailing)-1)
           n = int('{}{}'.format(leading,
                                 trailing))

def inversion_idx(N):
    num = str(N)
    if len(num) == 1:
        return None
    for c in range(len(num)-1,0,-1):
        if num[c]<num[c-1]:
            return (c-1)
    return None

def enumeration_solver(T, N=None):
    """
    Test all the numbers in reverse order
    """

    for n in range(N,1,-1):
        if inversion_idx(n) is None:
            return 'Case #{}: {}\n'.format(T,n)


if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '.out'

    try:
        with open(input_file, 'r') as f:
            T = read_int(f)  # Number of test cases
            for t in range(1, T + 1):
                sys.stdout.write(improved_enumeration_solver(**main_reader(t, f)))
    except IOError:
        print('File %s not found' % input_file)
        exit(1)
