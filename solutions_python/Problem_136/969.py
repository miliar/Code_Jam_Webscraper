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
  C, F, X = file.readline().split()
  C=float(C)
  F=float(F)
  X=float(X)
  
  cookie_rate=2
  time=[]
  time_to_win_with_factory=0
  time_to_win=1
  
  while time_to_win_with_factory<time_to_win:
      time.append(C/cookie_rate)
      
      time_to_win=(X-C)/cookie_rate
      time_to_win_with_factory=X/(cookie_rate+F)
  
      cookie_rate=cookie_rate+F 

  answer=sum(time)+time_to_win
      

  print "Case #%d: %s" % (t + 1, answer)

  
