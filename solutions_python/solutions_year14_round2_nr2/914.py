# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
import numpy as np
import scipy as sc
import itertools
import re
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
    return [reader(f, *args, **kwargs) for i in range(R)]


def main_reader(T,f):
    
    # Here need to read each individual test case.
    A,B,K = read_ints(f)
    return {'T':T,'A':A,'B':B,'K':K}    
    
def solver(T,A=None,B=None,K=None):
    """
    Test all integers bought,
    the candidates for the and operation should have both ones in the position
    of the ones of candidate and can have zeros in positions of the zeros
    alternatively
    """
    #for k in range(K):
    #    
    #    kbin = [int(t) for t in list(str(bin(k))[2:])]
    #    zero_idxs = np.where(kbin==0)
    #    kbin[zerp_idxs]=0
    #    for kk in range(len(zero_idxs)):
    #     ones_idxs =itertools.combinations(zero_idxs,kk)
    #     bits = 
        
def solver2(T,A=None,B=None,K=None):
    """
    Test all integers bought,
    the candidates for the and operation should have both ones in the position
    of the ones of candidate and can have zeros in positions of the zeros
    alternatively
    """
    cnt = 0
    for a in range(A):
        for b in range(B):
            if np.bitwise_and(a,b)<K:
                cnt +=1
   
    return 'Case #%s: %d\n' % (T, cnt)
    

if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file =  input_file.split('.')[0]+'.out'    
#    ff = open(output_file,'w')
    try:
      with open(input_file,'r') as f:
          T = read_int(f)
#    common = setup(sys.stdin)
          for t in range(1, T+1):
              sys.stdout.write(solver2(**main_reader(t,f)))
    except IOError:
       print 'File %s not found'%input_file
       exit(1)       

