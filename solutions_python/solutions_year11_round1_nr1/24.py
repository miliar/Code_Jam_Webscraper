#!/usr/bin/python
#a.py
#Author: James Damore
#Created on: May 20, 2011
#Time-stamp: <2011-05-20 21:09:01>
#cat Downloads/A-small-attempt0.in | ~/python/codeJam/1A/a.py > output.txt

import math
import string
import sys

def read_ints(lines = 1):
    if lines == 1: return map(int, raw_input().split())
    return [map(int, raw_input().split()) for _ in range(lines)]

def gcd(x, y):
  if x < y: (x, y) = (y, x)
  while y > 0:
      x = x % y
      (x, y) = (y, x) 
  return x


def read_input():
    N, P_D, P_G = read_ints()

    d = gcd(P_D, 100)
    denom = 100 / d
    if denom > N:
        return 'Broken'
    if P_G == 100 and P_D != 100:
        return 'Broken'
    if P_G == 0 and P_D != 0:
        return 'Broken'
    
    return 'Possible'


numCases=input()
for i in range(1, numCases+1):
    #read_input()
    output = read_input()
    print "Case #%d:" % i, output
