#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function
import numpy as np 

t = int(raw_input())


for ti in xrange(1, t+1):
  n = [c for c in raw_input()]
  a = np.array(n).astype(np.int)
  la = len(a)

  k = 1
  while k < la:
    if a[k]<a[k-1]:
      a[k-1] -= 1
      a[k:] = 9
      k = 1
      continue
    k += 1

  ans = 0
  for d in a:
    ans = ans*10+d
  
  print("Case #{}: {}".format(ti, ans))
