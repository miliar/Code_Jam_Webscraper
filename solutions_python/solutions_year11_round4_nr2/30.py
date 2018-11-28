from __future__ import division
import collections
import numpy as np

def test(sheet, R, C, K):
  max_R = R + K - 1
  max_C = C + K - 1
  center_R = (R + max_R + 1) / 2.
  center_C = (C + max_C + 1) / 2.
  
  disallowed = set([(R, C), (R, max_C), (max_R, C), (max_R, max_C)])
  
  mass_R = 0
  mass_C = 0
  for r in xrange(R, max_R + 1):
    for c in xrange(C, max_C + 1):
      if (r, c) in disallowed: continue
      m = sheet[r][c]
      mass_R += m * ((r + 0.5) - center_R)
      mass_C += m * ((c + 0.5) - center_C)
#  return abs(mass_R - 0) < 1e-6 and abs(mass_C - 0) < 1e-6
  return mass_R == 0 and mass_C == 0

f = open('B-small.in', 'r')
cases = int(f.next())
for i in xrange(cases):
  R, C, D = [int(x) for x in f.next().split()]
  sheet = np.ndarray((R,C), np.int32)
  for r in xrange(R):
    sheet[r] = [int(x) + D for x in iter(f.next().strip())]
  
  max_K = min(R, C)
  max_possible = 0
  for k in xrange(3, max_K + 1):
    # Test if blade of size k is feasible
    for r in xrange(0, R - k + 1):
      end = False
      for c in xrange(0, C - k + 1):
        if test(sheet, r, c, k):
          end = True
          max_possible = k
          break
      if end: break
  
  if max_possible == 0:
    print 'Case #%d: IMPOSSIBLE' % (i + 1)
  else:
    print 'Case #%d: %d' % (i + 1, max_possible)