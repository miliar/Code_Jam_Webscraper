#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function
from array import array

t = int(raw_input())

for ti in xrange(1, t+1):
  m, n = map(int, raw_input().split())
  
  cake = []
  for i in xrange(m):
    cake.append(array('c', raw_input()))

  for i in xrange(n):
    for j in xrange(m):
      if cake[j][i] == '?':
        dis = 100
        for k in xrange(m):
          if k==j: continue
          if cake[k][i] != '?' and abs(k-j)<dis:
            dis = abs(k-j)
            cake[j][i] = cake[k][i]

  for i in xrange(m):
    for j in xrange(n):
      if cake[i][j] == '?':
        dis = 100
        for k in xrange(n):
          if k==j: continue
          if cake[i][k] != '?' and abs(k-j)<dis:
            dis = abs(k-j)
            cake[i][j] = cake[i][k]
  
  print("Case #{}:".format(ti))
  for l in cake:
    print(l.tostring())
