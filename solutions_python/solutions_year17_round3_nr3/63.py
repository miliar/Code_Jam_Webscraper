#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function
import numpy as np

t = int(raw_input())

for ti in xrange(1, t+1):
  n, k = map(int, raw_input().split())
  u = float(raw_input())

  p = map(float, raw_input().split())
  
  p.append(1.0)
  p = np.array(p)
  p.sort()

  for i in xrange(n):
    d = p[i+1]-p[i]

    if d*(i+1)>u:
      p[:i+1] += u/(i+1)
      break
    else:
      p[:i+1] += d
      u -= d*(i+1)
    
  ans = 1.0

  for i in xrange(n):
    ans *= p[i]
  
  print("Case #{}: {:.6f}".format(ti, ans))
