# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
import numpy as np
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
    D, N = read_ints(f, d=' ')
    K = []
    S = []
    for _ in range(N):
      k,s = read_ints(f)
      K.append(k)
      S.append(s)

    return {'T': T,'D':D, 'N': N, 'S': S,'K':K}


def improved_enumeration_solver(T, K=None, S=None):
   """
   For large arrays where len(S)/K > 10 verify that is feasible 
   solving subarray length 2K con padding a 3K
   """
   print(len(S),K)
   if (float(len(S))/float(K))>3:
       res = enumeration_solver(T,K,S[0:3*K],max_flip_pos=2*K)
       if res.find("IMPOSSIBLE")>0:
           return res

   return enumeration_solver(T, K, S)

def simple_solver(T, D=None, N=None, K=None, S=None):
    """
    """
    S = np.array(S,dtype=np.float)
    K = np.array(K,dtype=np.float)
    #print(D,N,S,K)
    DR = D - K
    #print(DR)
    DR_S = DR/S
    #print(DR_S)
    amax= (np.argmax(DR_S))
    #print(amax)
    return 'Case #{}: {}\n'.format(T,D/DR_S[amax])
    #    cand = new_cand
    #    flips+= 1



        # return 'Case #%d: %s\n'%(T,' '.join([str(t) for t in tests]))


if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '.out'

    try:
        with open(input_file, 'r') as f:
            T = read_int(f)  # Number of test cases
            for t in range(1, T + 1):
                sys.stdout.write(simple_solver(**main_reader(t, f)))
    except IOError:
        print('File %s not found' % input_file)
        exit(1)
