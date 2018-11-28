# -*- coding: utf-8 -*-
"""
 
@author: Luca
"""

# General imports
import numpy as np
import scipy as sc
import itertools
import sys

#symbol_map = {'i':0,'j':1,'k':2}
matrix = {'1':{'1':('1',1),'i':('i',1),'j':('j',1),'k':('k',1)},\
          'i':{'1':('i',1),'i':('1',-1),'j':('k',1),'k':('j',-1)},\
          'j':{'1':('j',1),'i':('k',-1),'j':('1',-1),'k':('i',1)},\
          'k':{'1':('k',1),'i':('j',1),'j':('i',-1),'k':('1',-1)}}


next_req_val = {'i':'j','j':'k','k':None}

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
    L,X= read_ints(f)
    text = read_word(f)
    return {'T':T,'L':L,'X':X,'TEXT':text}    

def quaternion_mult(a,b):
## a and b are tuples of value and sign +1/-1
   res = matrix[a[0]][b[0]]
   if a[1]*b[1]<0:
      return (res[0],-1*res[1])
   else:
      return res

def test_seq(text,start_idx,end_idx,req_val):
# Retruns a list of lenghts of subsequences that evaluate to a given constant
    nn = start_idx
    tmp = ('1',1)    
    while True:
        tmp = quaternion_mult(tmp,(text[nn],1))
        if tmp == req_val:
            if req_val[0] == 'k':
                 if nn==len(text)-1:
                     #print 'valid k:%s'%(text[start_idx:])
                     return True
            elif  req_val[0] == 'j':        
                #print 'valid j:%s'%(text[start_idx:nn+1])
                return test_seq(text,nn+1,end_idx+1,('k',1))
            elif req_val[0] == 'i':
                #print 'valid i:%s'%(text[start_idx:nn+1])
                return test_seq(text,nn+1,end_idx+1,('j',1))
        nn +=1
        if nn>=end_idx:
            break
    return False
     
    
def naive_solver(T,L=None,X=None,TEXT=None):
# Enumeration
    ftext =TEXT*X
    #print 'string:%s'%ftext
    ll = len(ftext)    
    if len(ftext)<3:
        return 'Case #%s: %s\n' % (T, 'NO')    
    test = test_seq(ftext,0,ll-2,('i',1))
    if test == True:    
        return 'Case #%s: %s\n' % (T, 'YES')    
    else:        
        return 'Case #%s: %s\n' % (T, 'NO')    

if __name__ == '__main__':

    do_debug = True
    input_file = sys.argv[1]
    output_file =  input_file.split('.')[0]+'.out'    
    
    try:
      with open(input_file,'r') as f:
          T = read_int(f) # Number of test cases
          for t in range(1, T+1):
              sys.stdout.write(naive_solver(**main_reader(t,f)))
    except IOError:
       print 'File %s not found'%input_file
       exit(1)       

