# from math import *
for case in xrange(int(raw_input())):
  r,t=map(int,raw_input().split())
  res,i = 0,1
  while 1:
    t -= 2*r+i
    if t < 0: break
    res += 1
    i += 4
  print 'Case #%d: %d'%(case+1, res)
