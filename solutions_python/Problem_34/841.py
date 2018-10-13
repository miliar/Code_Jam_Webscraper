#!/usr/bin/env python

import sys
import string
import re

def check_string( rule , val ):
   rule_ = split_rule(rule)
   i = 0
   for r,r_ in rule_:
       if r_ == 1:
          if r.count(val[i]): 
             i+=1
          else:
             break
       else:
          for r1 in r:
             if r1 == val[i]:
                 i+=1
             else:
                 break 
          
   return len(val) == i 

def input_file( file_ ):
   out_ = []
   i_file = file(file_)

   LDN = i_file.readline() 

   L,D,N = LDN.split()

   L = int(L)
   D = int(D)
   N = int(N)

   d_str = []
   for i in range(D):
       d_str.append(i_file.readline())
       pass

   n_str = []
   for i in range(N):
       n_str.append(i_file.readline())
       pass

   check_i = 1
   for n_s in n_str:
      check_ok = 0
      for d_s in d_str:
         if check_string(n_s,d_s):  
            check_ok +=1
      out_.append("Case #%d: %d" % (check_i,check_ok))
      check_i +=1

   i_file.close()
   return out_

def split_rule( rule ):
   t1 = rule.split("(") 
   t = []
   for t2 in t1:
       if t2.count(")") > 0:
           t.append([t2.split(")")[0],1])
           t.append([t2.split(")")[1],0])
       elif len(t2) > 0 :
           t.append([t2,0])

   return t

if __name__ == "__main__":
   output = input_file("A-small-attempt5.in")
   for o in output: 
      print o
