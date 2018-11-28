#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
  cases += [map(int, fh.readline().strip().split(" "))]

try:
  cases += [map(int, fh.readline().strip().split(" "))]
except:
  print "good read"

fh.close()

#http://www.daniweb.com/code/snippet216539.html#

def Denary2Binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])



fh = open("out.txt","w")
for (i,case) in enumerate(cases):
  if "0" in int2bin(case[1],30)[-1*case[0]:]:
      print >> fh, "Case #"+str(i+1)+": OFF"
  else:
    print >> fh, "Case #"+str(i+1)+": ON"

fh.close()
