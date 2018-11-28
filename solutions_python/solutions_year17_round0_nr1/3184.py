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
    S, K = read_words(f, d=' ')
    K = int(K)
    return {'T': T, 'K': K, 'S': S}


def improved_enumeration_solver(T, K=None, C=None, S=None):
    """
   fourth in third and so on 
   """
    pass

def enumeration_solver(T, K=None, S=None):
    """
   Tries all the possible combinations of flipping:
   At each round are available len(S) - K + 1
   possible flip positions ranging from 
   0 to len(S) - K 
   """
    from bitstring import BitArray
    S = BitArray(bin=S.replace('+', '1').replace('-', '0'))
    solution = '1' * len(S)
    if S.bin == solution:
        return 'Case #{}: {}\n'.format(T, 0)

    #print('Case {}'.format(S.bin))
    cand = [S]
    flip_pos = range(len(S) - K + 1)
    flips = 1
    explored = {S.bin}
    while flips > 0:
        #print('Round {} Candidates {}'.format(flips,len(cand)))
        new_cand = []
        for c in cand:
            for f in flip_pos:
                flipped = BitArray(c)
                flipped.invert(range(f, f + K))
                if flipped.bin == solution:
                    return 'Case #{}: {}\n'.format(T, flips)
                if flipped.bin not in explored:
                    new_cand.append(flipped)
                    explored.add(flipped.bin)
        if len(new_cand) == 0:
            return 'Case #{}: IMPOSSIBLE\n'.format(T)
        cand = new_cand
        flips+= 1



        # return 'Case #%d: %s\n'%(T,' '.join([str(t) for t in tests]))


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
