#!/usr/bin/python

import os
import sys
import math

def read_input_NN(fn =""):
  fh = open(fn, "r")
  lines = map(lambda x: x.strip(), fh.readlines())
  fh.close()
  goog_N = map(int, lines[0].split())[0]
  l_dict = lines[1:]
  return(l_dict)

def sum_square(str1="123"):
  sum1 = 0
  for i in str1:
    sum1 += int(i)*int(i)
  return(sum1)

def tobase(base,number):
    global tb
    #http://myphotoblogbeta.blogspot.com/2007/07/python-convert-to-and-from-base-b.html
    def tb(b,n,result=''):
        if n == 0: return result
        else: return tb(b,n/b,str(n%b)+result)
    if type(base) != type(1):
        raise TypeError, 'invalid base for tobase()'
    if base <= 0:
        raise ValueError, 'invalid base for tobase(): %s' % base
    if type(number) != type(1) and type(number) != type(1L):
        raise TypeError, 'tobase() of non-integer'
    if number == 0:
        return '0'
    if number > 0:
        return tb(base, number)
    if number < 0:
        return '-' + tb(base, -1*number)

def determine_happy(base1 = 10,num1 = "83"):
  last_num="0"
  d_found = {}
  num1 = tobase(base1,int(num1))
  #print num1
  while(num1!="1"):
    num1 = tobase(base1,sum_square(num1))
    #print num1
    if last_num == num1:
      break
    if num1 == "1":
      break
    last_num = num1
    if num1 in d_found.keys():
      break
    d_found[num1]=1
  if num1 == "1":
    return(1)
  return(0)

def find_smallest(l2=[1,2,3]):
  i_c=1
  l2 = filter(lambda x: x!=2, l2)
  if len(l2) == 0:
    return(1)
  for i in xrange(2,1000000):
    #print i
    #print l2
    i_c=i
    i_s = str(i)
    is_happy = map(lambda x: determine_happy(x,str(i)),l2)
    #print is_happy
    prod = 1
    for j in is_happy:
      prod *= j
    if prod == 1:
      break
  return(i_c)

def small_base(str1="123"):
  l2 = list(str1)
  #print l2
  set1 = set(l2)
  d_map={}
  dec_list = [1,0]+range(2,100)
  dec_i = 0
  for i in l2:
    if i not in d_map.keys():
      d_map[i]=dec_list[dec_i]
      dec_i+=1
  #print d_map
  l2 = map(lambda x: d_map[x],l2)
  #print l2
  base1 = max([2,len(set1)])
  #print base1
  num1 = 0
  for (ctr,i) in enumerate(l2[::-1]):
    num1+=math.pow(base1,ctr)*i
  return(num1)

def qa(fn="sample"):
  l1 = read_input_NN(fn)
  #print l1
  return(l1)

#l1 = qa(fn="A-large.in.txt")
l1 = qa(fn="A-small-attempt0-1.in.txt")
#print l1
fh = open("out.txt","w")
for (ctr,sol) in enumerate(l1):
  print >> fh, "Case #"+str(ctr+1)+": "+str(int(small_base(sol)+.001))
  #print small_base(sol)

fh.close()
