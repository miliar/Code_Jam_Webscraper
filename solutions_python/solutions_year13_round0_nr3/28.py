#!/usr/bin/python
from math import *

pals = {}

def pal(x):
  s = str(x)
  for i in xrange(len(s)/2):
    if s[i] <> s[-1-i]:
      return False
  return True

def go(x):
  if pal(x*x):
    pals[x] = True

def gen(x,y,lev,ones):
  if (x>10**25 or ones > 4):
    return

  gen(x*10+0,y+0*lev,lev*10,ones+0)
  gen(x*10+1,y+1*lev,lev*10,ones+1)

  go(x*lev+y)
  go(x*lev*10+0*lev+y)
  go(x*lev*10+1*lev+y)
  go(x*lev*10+2*lev+y)

for i in xrange(10):
  go(i)
gen(1,1,10,0)
gen(2,2,10,0)
gen(3,3,10,0)

nums = [-5,-6] + sorted(pals.keys()) + [10**108+5, 10**108+6]

def get(y):
  global nums

  x = 0
  radius = 2**20
  while radius >= 1:
    pos = x + radius
    if pos < len(nums) and nums[pos] * nums[pos] <= y:
      x = pos
    radius /= 2
  return x

tests = long(raw_input())
for i in xrange(1,1+tests):
  x,y = map(long, raw_input().split())
  print "Case #" + str(i) + ": " + str(get(y) - get(x-1))


