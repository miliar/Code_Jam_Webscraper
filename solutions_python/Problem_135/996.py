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
  guess1 = int(file.readline())
  for i in range(4):
      temp=file.readline()
      if i==guess1-1:
          line1=temp.split()
  guess2 = int(file.readline())
  for i in range(4):
      temp=file.readline()
      if i==guess2-1:
          line2=temp.split() 
  answer=set(line1).intersection(set(line2)) 
  if len(answer)==1:
     print "Case #%d: %s" % (t + 1, int(answer.pop()))
  elif len(answer)==0:
     print "Case #%d: Volunteer cheated!" % (t + 1) 
  elif len(answer)>1:
     print "Case #%d: Bad magician!" % (t + 1) 
  
