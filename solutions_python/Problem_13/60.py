#!/usr/bin/python

import sys
import math

try:
  import psyco
  psyco.full()
except Exception, e:
  pass

IMPOSSIBLE = 2 ** 31

def is_impossible(x):
  return x >= IMPOSSIBLE

MEMO = {}

def solve(tree, change, wanted, i, interior_range):
   if i >= interior_range:
     if wanted == tree[i]:
       return 0
     else:
       return IMPOSSIBLE

   if MEMO.has_key((wanted, i)):
     return MEMO[(wanted, i)]

   funct = [(tree[i], 0)] # func, cost
   if change[i]:
     funct.append((1 - tree[i], 1))

   results = []

   for f, w in funct:
     if f == 1: # AND
       if wanted == 0:
         w0 = solve(tree, change, 0, i * 2 + 1, interior_range)
         if w0 > 0:
           w0 = min(w0, solve(tree, change, 0, i * 2 + 2, interior_range))
         if w0 + w == 0:
           return 0
         results.append(w0 +  w)
       else: # wanted 1
         w0 = solve(tree, change, 1, i * 2 + 1, interior_range)
         if not is_impossible(w0):
           w0 += solve(tree, change, 1, i * 2 + 2, interior_range)
         if w0 + w == 0:
           return 0
         results.append(w0 +  w)
     else: # OR
       if wanted == 0:
         w0 = solve(tree, change, 0, i * 2 + 1, interior_range)
         if not is_impossible(w0):
           w0 += solve(tree, change, 0, i * 2 + 2, interior_range)
         if w0 + w == 0:
           return 0
         results.append(w0 +  w)
       else :#wanted 1
         w0 = solve(tree, change, 1, i * 2 + 1, interior_range)
         if w0 > 0:
           w0 = min(w0, solve(tree, change, 1, i * 2 + 2, interior_range))
         if w0 + w == 0:
           return 0
         results.append(w0 +  w)

   r = min(results)
   MEMO[(wanted, i)] = r
   return r

if __name__ == '__main__':
  if len(sys.argv) != 2:
     print ('Usage: %s file' % sys.argv[0])
     sys.exit(1)

  f = open(sys.argv[1])
  NTEST =  int(f.readline())
  for i in xrange(NTEST):
    MEMO = {}
    print ('Case #%d:' % (i + 1)),
    M, V = map(int, f.readline().strip().split())
    tree = []
    change = []
    for i in xrange(M):
      if i < (M - 1) / 2:
        comp, c = map(int, f.readline().strip().split())
        tree.append(comp)
        change.append(c)
      else:
        tree.append(int(f.readline()))
    r = solve(tree, change, V, 0, (M - 1) / 2)
    if is_impossible(r):
      r = 'IMPOSSIBLE'
    print r
    #print >> sys.stderr, MEMO
    #sys.exit(1)
