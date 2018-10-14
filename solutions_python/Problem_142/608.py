#!/usr/bin/env python
import os
import sys
import time

tStart = time.time()

#---------------------------------------------------------------------

ifilename = 'input.in'
ofilename = 'results.out'

args = sys.argv
if len(args) > 1:
  ifilename = args[1]
if len(args) > 2:
  ofilename = args[2]

#---------------------------------------------------------------------
 
ifile = open(ifilename,'r')
data  = ifile.read()
ifile.close()
lines = data.splitlines()

ofile = open(ofilename, 'w')

#---------------------------------------------------------------------

def reduce_word(w1):
  ww = [1]
  w2 = [w1[0]]
  for x in w1[1:]:
    if x != w2[-1]:
      w2     += [x]
      ww     += [1]
    else:
      ww[-1] += 1
  return w2, ww

def diffs(refw, ws):
  s = 0
  for w in ws:
    for k,x in enumerate(w):
      s += abs(x-refw[k])
  return s



ncases = int(lines[0])
lines  = lines[1:]
for n in xrange(ncases):
  n_strings = int(lines[0])
  lines     = lines[1:]
  words     = [lines[k] for k in xrange(n_strings)]
  lines     = lines[n_strings:]

  res = '0'
  weights = []
  for k,w in enumerate(words):
    key, weight  = reduce_word(w)
    weights     += [weight]
    if k == 0:
      ref_key = key
    else:
      if key != ref_key:
        res = 'Fegla Won'
        break

  if res == '0':
    ref_w = [0 for k in xrange(len(weights[0]))]
    for w in weights:
      for k,x in enumerate(w):
        ref_w[k] += x
    ref_w = [int(x/len(weights)) for x in ref_w]

    ref_changes = diffs(ref_w, weights)
    
    for k in xrange(len(ref_w)):
      for ss in xrange(2):
        new_w       = [x for x in ref_w]
        new_w[k]   += 1-2*ss
        new_changes = diffs(ref_w, weights)
        while ref_changes > new_changes:
          ref_changes = new_changes
          ref_w       = [x for x in new_w]
          new_w[k]   += 1-2*ss
    res = '%d'%(ref_changes)


  # -------------------------------------------------
  res = 'Case #%d: %s'%(n+1, res)
  ofile.write('%s\n'%(res))
  print res

#---------------------------------------------------------------------

ofile.close()

print '\n Run time = ' + str((time.time() - tStart))     
