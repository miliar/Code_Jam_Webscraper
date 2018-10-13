#!/usr/bin/env python
import math
from decimal import *
import itertools

def side_area(p):
  return Decimal(2)*Decimal(math.pi)*Decimal(p[0])*Decimal(p[1])

def top_area(p):
  return Decimal(math.pi)*Decimal(p[0])*Decimal(p[0])

def stack_area(stack):
  stack.sort(key=lambda x: x[0], reverse=True) 
  sa = top_area(stack[0])
  for i in range(len(stack)):
     sa+=side_area(stack[i])
  return sa
  

cases = raw_input()
for ca in range(int(cases)):
    (n,k) = raw_input().strip().split()
    n=int(n); k=int(k)

    pancakes = []
    for i in range(n):
      (r,h) = raw_input().strip().split()
      r=int(r);h=int(h)
      pancakes.append((r,h))
      #print "pancake:",i,r,h
      #print "side area",side_area(r,h)

   
    
    sa = ""
    if(n==k): # special case, use all pancakes
      sa = stack_area(pancakes)


    # otherwise try them all
    else:
      combos = itertools.combinations(pancakes,k)
      best_stack_area = 0
      best_stack= []
      for c in combos:
        sac = stack_area(list(c)) 
        if sac>best_stack_area:
          best_stack_area=sac
          best_stack = c
          
      sa = best_stack_area

    # 
      ##print pancakes 
    

    print "Case #%i: %s" % ( (ca+1), str(sa))
