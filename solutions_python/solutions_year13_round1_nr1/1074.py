from bigfloat import *
import math
import sys
f = open(sys.argv[-1], 'r')
lines = f.readlines()
num_tests = lines[0]

case_num = 0
for case in lines[1:]:
  case_num += 1
  sum = 0
  s = case.split()
  r = float(s[0])
  t = float(s[1])
  ans = (sqrt(4*r*r-4*r+8*t+1, precision(100))-2*r+1)/4
  print "Case #%s: %i"%(case_num, math.floor(ans))
