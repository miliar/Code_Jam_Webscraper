#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function

t = int(raw_input())

for ti in xrange(1, t+1):
  n, p = map(int, raw_input().split())
  group = map(int, raw_input().split())

  
  if p == 2:

    ans = 0
    cnt = 0

    for v in group:
      if (v&1) == 0:
        ans += 1
      else:
        cnt += 1

    ans += (cnt+1)/2
  elif p == 3:
    
    ans = 0
    cnt1 = 0
    cnt2 = 0

    for v in group:
      u = v%3

      if u == 0:
        ans += 1
      elif u == 1:
        cnt1 += 1
      else:
        cnt2 += 1

    minv = min(cnt1, cnt2)
    maxv = max(cnt1, cnt2)

    ans += minv + (maxv-minv+2)/3
  
  print("Case #{}: {}".format(ti, ans))
