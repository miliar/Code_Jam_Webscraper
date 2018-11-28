# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:02:27 2013

@author: slonny
"""
from sys import argv

script, filename = argv
file = open(filename)
T = int(file.readline())

for t in range(T):
  block_n=int(file.readline())
  Naomi=file.readline().split()
  Ken=file.readline().split() 
  Naomi=sorted(Naomi)
  Ken=sorted(Ken)
  
  answer=[]
  
  p1=Naomi
  p2=Ken
  for k in range(2):
      p2counter=0
      p1counter=0
      main_counter=0
    
      while p2counter<len(p1):
          if p1[p2counter]>p2[p1counter]:
              main_counter+=1
              p2counter+=1
              p1counter+=1
          else:
              p2counter+=1
                  
      answer.append(main_counter)
      
      p1=Ken
      p2=Naomi
  

  print "Case #%d: %s %s" % (t + 1, answer[0], len(p1)-answer[1])

  
