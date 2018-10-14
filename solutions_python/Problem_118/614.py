#!/usr/bin/pypy
import sys
import math
import fractions
import pickle
from array import array
from operator import itemgetter
from bisect import *

def rl(convert=''):
  line = sys.stdin.readline().split()
  for i,c in enumerate(convert):
    if c=='i':
      line[i]=int(line[i])
    elif c=='s':
      pass
    elif c=='f':
      line[i]=float(line[i])
  # if len(line)==1:
  #   return line[0]
  return line

def gcd(*args):  
  if len(args)==0:
    return 0
  g = args[0]
  for i in range(1,len(args)):
    g = fractions.gcd(g,args[i])    
  return g

def lcm(*args):
  if len(args)==0:
    return 0
  g = args[0]
  for i in range(1,len(args)):
    g *= args[i]  
  return g/gcd(*args)


# def find_le(a, x):
#     'Find rightmost value less than or equal to x'
#     i = bisect_right(a, x)
#     print i
#     if i:
#         return i-1

# def find_ge(a, x):
#     'Find leftmost item greater than or equal to x'
#     i = bisect_left(a, x)
#     if i != len(a):
#         return i

#--------------------------------------------------------------------#

# lst = list()
# for i in range(0, 10**8+1):    
#     if str(i)==str(i)[::-1]:
#       c = str(i*i)
#       if c==c[::-1]:
#         lst.append(i*i)

# print(lst)

# sys.stderr.write('List generated')

# f = open('fancy.dat','wb')
# pickle.dump(lst,f,2)
# f.close()

f = open('fancy.dat','rb')
lst = pickle.load(f)
f.close()


t = rl('i')[0]

for index in range(1,t+1):
  s = 0
  a,b = rl('ii')
  # print a,b
  s = bisect_right(lst, b)-bisect_left(lst, a)  
  print('Case #%(i)d: %(res)d' % {'i':index, 'res':s})
