#!/usr/bin/python
import sys
from sets import Set


f = sys.stdin
N = int(f.readline())
w = 'welcome to code jam'

for case in xrange(1, N+1):
  s = f.readline()
  s = s[:-1]
  cnt = 19*[0]
  for c in s:
    for j in xrange(18, 0, -1):
      if c == w[j]:
        cnt[j] = (cnt[j]+cnt[j-1])%10000
    if c == 'w':
      cnt[0] += 1
  print 'Case #%d: %04d' % (case, cnt[-1])

