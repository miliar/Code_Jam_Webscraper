# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:02:27 2013

@author: slonny
"""
from sys import argv
from collections import Counter
from collections import OrderedDict
import numpy


script, filename = argv

file = open(filename)

T = int(file.readline())


for t in xrange(T):
  A, B, K = file.readline().split()
  A=int(A)
  B=int(B)
  K=int(K)
  
  counter=0
  
  min_t=min(A, B)-1
  max_t=max(A, B)-1
  
  for i in xrange(K, A):
      for j in xrange(K, B):
          result=i&j
          if result>=K:
              counter=counter+1


  print "Case #%d: %d" % (t + 1, A*B-counter)
          
      
 
      

  

     


