#!/usr/bin/python

from collections import OrderedDict
import sys

input_file = open(sys.argv[1], "r")
flag = 0 # toss 1rst line
case = 1
wins = 0
for line in input_file:
 if flag == 1:
  token = line.split()
  A = long(token[0])
  B = long(token[1])
  K = long(token[2])
  
  list_ = []
  for x in range(0,A):
   for y in range(0,B):
    z = x & y
    if ( z < K ):
     list_.append(z)


#  for x in range(0,B):
#   for y in range(0,A):
#    z = x & y
#    if ( z < K ):
#     list_.append(z)
  print ("Case #{0}: {1}".format(case, len(list_)))
  case = case + 1
  
 
 flag = 1
