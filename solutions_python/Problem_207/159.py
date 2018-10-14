#!/usr/bin/env python

import sys
import numpy as np

inputs = [line.strip() for line in sys.stdin]

T = int(inputs[0])

for t in xrange(T):
  # solve the input
  
  N, R, O, Y, G, B, V = [int(x) for x in inputs[t+1].split()]

  ##### REDUCING TO RYB
  if R == G and R + G == N:
    print "Case #{0}: {1}".format(t+1, "".join(R*['RG']))
    continue
  if B == O and B + O == N:
    print "Case #{0}: {1}".format(t+1, "".join(B*['BO']))
    continue
  if Y == V and Y + V == N:
    print "Case #{0}: {1}".format(t+1, "".join(Y*['YV']))
    continue

  if (R - G) <= 0 and (R!=0 or G!=0):
    print "Case #{0}: IMPOSSIBLE".format(t+1)
    continue
  R = R - G
  # we have G times 'RGR'

  if (B - O) <= 0 and (B!=0 or O!=0):
    print "Case #{0}: IMPOSSIBLE".format(t+1)
    continue
  B = B - O
  # we have O times 'BOB'

  if (Y - V) <= 0 and (Y!=0 or V!=0):
    print "Case #{0}: IMPOSSIBLE".format(t+1)
    continue
  Y = Y - V

  ##### SOLVING THE RYB CASE
  
  maxim = max(R,Y,B)
  if 2*maxim > R + Y + B:
    # two maxims forced to be next to each other
    print "Case #{0}: IMPOSSIBLE".format(t+1)
    continue

  minim = min(R,Y,B)
  mid = R + Y + B - maxim - minim

  if R == maxim:
    maxStr = 'R'
  elif Y == maxim:
    maxStr = 'Y'
  else:
    maxStr = 'B'

  if R == mid and maxStr != 'R':
      midStr = 'R'
  elif Y == mid and maxStr != 'Y':
    midStr = 'Y'
  else:
    midStr = 'B'

  if maxStr != 'R' and midStr != 'R':
    minStr = 'R'
  if maxStr != 'Y' and midStr != 'Y':
    minStr = 'Y'
  if maxStr != 'B' and midStr != 'B':
    minStr = 'B'

  out = maxim * [maxStr]

  for s in xrange(mid):
    out[s] += midStr

  for s in xrange(minim):
    out[len(out)-s-1] += minStr

  strOut = "".join(out)
  #####

  ##### PUT BACK THE O, G, V
  paste = "".join(G * ['GR'])
  ind = strOut.find('R')
  temp = strOut[0:(ind+1)] + paste 
  if ind + 1 < len(strOut):
    temp = temp + strOut[(ind+1):]
  strOut = temp

  paste = "".join(O * ['OB'])
  ind = strOut.find('B')
  temp = strOut[0:(ind+1)] + paste 
  if ind + 1 < len(strOut):
    temp = temp + strOut[(ind+1):]
  strOut = temp

  paste = "".join(V * ['VY'])
  ind = strOut.find('Y')
  temp = strOut[0:(ind+1)] + paste 
  if ind + 1 < len(strOut):
    temp = temp + strOut[(ind+1):]
  strOut = temp

  print "Case #{0}: {1}".format(t+1, strOut)
