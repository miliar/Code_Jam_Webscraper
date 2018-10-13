#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from __future__ import with_statement
import sys
import os

nb = 1

with open("./"+sys.argv[1], 'r') as fin:  
  with open("./"+sys.argv[2], 'w') as fout:
    T = int(fin.readline())
    for i in range(T):
      N = int(fin.readline())
      liste = [int(i) for i in fin.readline().split(" ")]
      liste.sort()
      xor_sean = 0
      xor_patrick = 0
      value = 0
      for j in range(N):
        xor_sean = xor_sean ^ liste[j]
        value = value + liste[j]
      if xor_sean >0 :
        fout.write("Case #"+str(nb)+": NO\n")  
        nb = nb+1
      else:
        for j in range(N):
          xor_sean = xor_sean ^ liste[j]
          xor_patrick = xor_patrick ^ liste[j]
          value = value - liste[j]
          if xor_sean == xor_patrick:
            fout.write("Case #"+str(nb)+": "+str(value)+"\n")  
            nb = nb + 1
            break

  
    
    
  

