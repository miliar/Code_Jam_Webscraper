import numpy as np
import sys, os
import math

rl = sys.stdin.readline

T = int(rl())
#T = 29

#===============================================================================
# print T
# for t in xrange(T):
#  L, P, C = map(int, rl().split())
#  print 'L:', L, 'P:', P, 'C:', C
#  tests = 0
#  while P > L * C:
#    tests += 1 
#    tp = math.log(1.0* P / L) / math.log(C) / 2
#    L = C ** tp
#    print 'L:', L, 'P:', P
#    print 'tp', tp
#    
#==============================================================================


for t in xrange(T):
  N = int(rl())
  A = []
  B = []
  for n in range(N):
    An, Bn = map(int, rl().split())
    A.append(An)
    B.append(Bn)

  ints = 0
  for i in range(N):
    for j in range(i,N):
      if ( A[i] > A[j] and B[i] < B[j] ) or (B[i] > B[j] and A[i] < A[j]):
        ints += 1
        
        
  print 'Case #%i: %i' % (t+1, ints)