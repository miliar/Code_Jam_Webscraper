#!/usr/bin/env python

import sys
import numpy as np

T = int(raw_input())

for t in xrange(T):
  # solve the input
  N, P = raw_input().strip().split()
  N = int(N)
  P = int(P)

  G = [int(x) for x in raw_input().strip().split()]
  mods = np.array([ x % P for x in G ])

  if P == 2:
    singles = np.sum(mods == 0)
    K = np.sum(mods == 1)
    out = singles + (K+1) / 2
    print "Case #{0}: {1}".format(t+1, out)
    continue

  if P == 3:
    K = np.sum(mods == 1)
    L = np.sum(mods == 2)

    singles = np.sum(mods == 0)
    pairs = min(K,L)
    
    rem = max(K,L) - min(K,L)    
    triples = rem / 3

    out = singles + pairs + triples
    if rem % 3 != 0:
      out += 1

    print "Case #{0}: {1}".format(t+1, out)
    continue

  if P == 4:
    J = np.sum(mods == 0)
    K = np.sum(mods == 1)
    L = np.sum(mods == 2)
    M = np.sum(mods == 3)

    out = 0

    out += J # singles first

    out += min(K,M) # pairs 1,3
    rem = max(K,M) - min(K,M)

    out += L / 2 # pairs 2,2
    two = L % 2

    if two == 1: # connect 1,1,2 or 3,3,2 ; if rem < 2, then just add (1), 2
      rem -= 2
      out += 1
      
    if rem > 0:
      # only rem things are remaining, can group to groups of 4
      out += rem / 4
      if rem % 4 != 0:
        out += 1

    print "Case #{0}: {1}".format(t+1, out)
