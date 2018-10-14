#!/usr/bin/python

import os,sys,string
import math

# solves the quadratic 
def solve_quadratic_floor(a,b,c):
  return math.floor(float((-b+(b**2-4*a*c)**0.5)/(2*a)))
  
def chk_quadratic_sign(a,b,c,y):
  val=a*y**2+b*y+c
  if val<=0:
    return 1
  if val>0:
    return 0

fname=sys.argv[1]
fhandle=open(fname,"r")

ncases=int(fhandle.readline())

for case in range(ncases):
  prefix="Case #"+str(case+1)+": "

  [r,t] = [int(k) for k in fhandle.readline().split(" ")]

  # solve 2 y^2 + (2r - 1) y - t == 0
  a = 2.0
  b = 2*r-1
  c = -1*t
  y = int(solve_quadratic_floor(a,b,c))

  # it doesn't work that well when the numbers are large, since we have precision problems
  # with floating point operations
  # but the estimates for y is good.
  max_y=0
  for temp_y in range(y-1,y+2):
    if chk_quadratic_sign(a,b,c,temp_y):
      max_y = temp_y
      
  print prefix+str(max_y)

