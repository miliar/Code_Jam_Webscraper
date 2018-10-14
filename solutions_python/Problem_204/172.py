#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function
import numpy as np 

t = int(raw_input())


for ti in xrange(1, t+1):
  n, p = map(int, raw_input().split())
  gre = np.array(map(int, raw_input().split()), dtype=np.int)

  quan = []
  for i in xrange(n):
    quan.append(np.array(map(int, raw_input().split()), dtype=np.float)/gre[i])
    quan[-1].sort()

  idx = np.array([0]*n, dtype=np.int)

  cnt = 0
  while np.all(idx<p):
    minr = 0
    minv = quan[0][idx[0]]
    for i in xrange(1, n):
      if minv > quan[i][idx[i]]:
        minv = quan[i][idx[i]]
        minr = i

    l = int(np.ceil(quan[minr][idx[minr]]/1.1))
    r = int(np.floor(quan[minr][idx[minr]]/0.9))

    for i in xrange(n):
      tl = int(np.ceil(quan[i][idx[i]]/1.1))
      tr = int(np.floor(quan[i][idx[i]]/0.9))
      
      l = max(l, tl)
      r = min(r, tr)

      if r < l: break
      
    if l <= r:
      for i in xrange(n):
        idx[i] += 1
  
      cnt += 1
    else:
      idx[minr] += 1
  print("Case #{}: {}".format(ti, cnt))
