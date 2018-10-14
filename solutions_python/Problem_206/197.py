#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function

t = int(raw_input())


for ti in xrange(1, t+1):
  d, n = map(int, raw_input().split())

  lt = 0

  for i in xrange(n):
    k, s = map(float, raw_input().split())
    tm = (d-k)/s
    lt = max(lt, tm)
  
  print("Case #{}: {:6f}".format(ti, d/lt))
