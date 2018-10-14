# -*- coding: utf-8 -*-
import sys
import itertools
import operator
import collections
from functools import reduce
def DoIt(points, rP, rS, l, p1, eP, eS):
  """ points: points for Sean in this try
  rP, rS: the actual subsets for patrick (1) and Sean(2) in binary
  representation. rP[i] is the i'th bit.
  l: the length on which we work in this iteration
  p1: all candies
  eP, eS: empty (True) or not (false)
  """
  best_new = -1                 # the best solution found in this recursion
  # find the length L for which we really have candies or finish
  # if we finish: check that both sets are non-empty and equal. 
  # If YES: return points of this solution
  # If No: return -1 (not solved)
  L = -1
  for i in reversed(sorted(list(p1.keys()))):
    if i <= l:
      L = i
      break
  if L==-1:
    if not eS and not eP and rP == rS:
      #print("Found solution: %d"%points)
      return points
    else:
      return -1
  S = p1[L]        
  S_coll = collections.Counter(S)
  # in order to "solve" this bit, we need that the total sum of bits is even
  # if not, return "-1" (not solved)
  if (len(S) +int(rP[L-1])+int(rS[L-1]))%2 != 0:
    return -1
  # Loop over all combinations for this length. They can have length's n from 0
  # up to len(S).  The combinations are then stored in "i"
  for n in range(0,len(S)+1):
    for i in itertools.combinations(S, n):
      # sum the elements using patricks & seans rule
      x, y, xb, yb = 0,0,0,0
      eP1, eS1 = eP, eS
      if n > 0: 
        xb = reduce(operator.xor, i)
        x = reduce(operator.add, i)
        eP1 = False
      if n < len(S):
        S_C = S_coll - collections.Counter(i)
#        print(S_C)
        j = list(S_C.elements())
#        print(j)
        if len(j) != 0:
          yb = reduce(operator.xor, j)
          y = reduce(operator.add, j)
          eS1 = False
      xb1, yb1 = [list(list(map(int,reversed(list(bin(x)[2:]))))) for x in [xb,yb]]
      xb = [0 for i in range(L_max)]
      yb = [0 for i in range(L_max)]
      for i,j in enumerate(xb1):
        xb[i] = j
      for i,j in enumerate(yb1):
        yb[i] = j
      # calculate the new sets rP1 and rS1 which will be tried. They are
      # obtained by adding xb and yb to rP and rS. y is added to points
      rP1 = rP[:]
      for i,j in enumerate(xb):
        rP1[i] ^= j
      rS1 = rS[:]
      for i,j in enumerate(yb):
        rS1[i] ^= j
      points1 = points +y
      #print "%s %s %d gives %s %s %d" %(rP,rS, points,rP1, rS1, points1)
      assert rP1[L-1] == rS1[L-1]
      res = DoIt(points1, rP1, rS1, L-1, p1, eP1, eS1)
      if res > best_new:
        best_new = res
#  print "finished this iteration %d. Best is %d"%(L,best_new)
  return best_new

f = open(sys.argv[1],"r")
T = int(f.readline())
for t in range(T):
  N = int(f.readline())
  pieces = list(map(int,f.readline().split()))
  assert len(pieces) == N
  pieces.sort()
  pieces.reverse()
  pieces_bin = [bin(x)[2:] for x in pieces]
  p1 = {}
  p1_bin = {}
  for p,pb in zip(pieces,pieces_bin):
    l = len(pb)
    if l in p1:
      p1[l].append(p)
      p1_bin[l].append(p)
    else:
      p1[l] = [p]
      p1_bin[l] = [p1]
  L_max = max(p1.keys())
  res1 = reduce(operator.xor, pieces)
  if res1 != 0:
    print("Case #%d: NO"%(t+1))
    continue
#  print(p1)
  res = DoIt(0,
    [0 for i in range(L_max)],
    [0 for i in range(L_max)],
    L_max, p1, True, True)
  if res == -1:
    assert res1 != 0
  else:
    print("Case #%d: %d"%(t+1, res))
    assert res1 == 0

