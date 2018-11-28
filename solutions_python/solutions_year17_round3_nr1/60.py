#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function
import math

t = int(raw_input())

for ti in xrange(1, t+1):
  n, k = map(int, raw_input().split())

  panc = []

  for i in xrange(n):
    r, h = map(float, raw_input().split())

    panc.append((r, h))
  
  panc.sort(key=lambda x: x[0]*x[1], reverse=True)

  maxr = 0.0
  ans = 0.0
  for i in xrange(k-1):
    maxr = max(maxr, panc[i][0])
    ans += 2.0*math.pi*panc[i][0]*panc[i][1]

  maxp = 0.0
  for i in xrange(k-1, n):
    tmpa = math.pi*(panc[i][0]**2) if panc[i][0]>maxr else math.pi*(maxr**2)
    tmpa += 2.0*math.pi*panc[i][0]*panc[i][1]
    maxp = max(maxp, tmpa)

  ans += maxp
  
  print("Case #{}: {:.9f}".format(ti, ans))
