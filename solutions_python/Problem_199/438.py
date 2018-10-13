#!/usr/bin/python

import sys, string

def flip(S,K):
  flipper = string.maketrans('-+','+-')
  l = len(S)
  left = S.find('-')
  right = S.rfind('-')
  flips = 0
  while left >= 0 and left+K<=l and left <= right-K+1:
    if left <= l-right:
      flip_pos = left
    else:
      flip_pos = right-K+1

    S=S[:flip_pos]+S[flip_pos:flip_pos+K].translate(flipper)+S[flip_pos+K:]
    left = S.find('-')
    right = S.rfind('-')
    flips += 1

  if left >= 0:
    return 'IMPOSSIBLE'
  else:
    return flips

dataset=open(sys.argv[1], 'r')
T=int(dataset.readline())
for t in xrange(1,T+1):
  (S,K)=dataset.readline().strip().split()
  K=int(K)
  print "Case #%d: %s"%(t, flip(S,K))
