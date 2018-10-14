#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function
import numpy as np

t = int(raw_input())


for ti in xrange(1, t+1):
  n, k = map(int, raw_input().split())

  acc = 0
  val = np.zeros((2, 2)).astype(np.int)
  val[0, 1] = 1
  l = r = 0

  while True:
    acc += val[0, 1]
    if acc >= k:
      if n&1:
        l = r = n/2
      else: 
        l = n/2
        r = n/2 - 1
      break
    acc += val[0, 0]
    if acc >= k:
      if (n-1)&1:
        l = r = (n-1)/2
      else: 
        l = (n-1)/2
        r = (n-1)/2 - 1
      break

    if n&1:
      val[1, 0] = val[0, 0]
      val[1, 1] = 2*val[0, 1]+val[0, 0]
    else:
      val[1, 0] = 2*val[0, 0]+val[0, 1]
      val[1, 1] = val[0, 1]

    n /= 2
    val[0] = val[1]
  
  print("Case #{}: {} {}".format(ti, l, r))
