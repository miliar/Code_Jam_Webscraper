# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
import numpy as np
import scipy as sc
import itertools
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
    SMAX,data = read_words(f)
    SMAX = int(SMAX)
    #data = np.array(read_arr(f,SMAX+1,reader=read_ints))
    vals = np.zeros((SMAX+1),dtype=np.int)        
    for i in range(0,SMAX+1):
        vals[i]=int(data[i])
    return {'T':T,'SMAX':SMAX,'VALS':vals}    
    
def solver(T,SMAX=None,VALS=None):
    standup = 0
    invited = 0
    for ss in range(0,SMAX+1):
        if standup>=ss:
            standup+=VALS[ss]
        elif VALS[ss]>0:
            invited += ss-standup
            standup += ss-standup +VALS[ss]
    return 'Case #%s: %d\n' % (T, invited)    

if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file =  input_file.split('.')[0]+'.out'    
    
    try:
      with open(input_file,'r') as f:
          T = read_int(f) # Number of test cases
#    common = setup(sys.stdin)
          for t in range(1, T+1):
              sys.stdout.write(solver(**main_reader(t,f)))
    except IOError:
       print 'File %s not found'%input_file
       exit(1)       

