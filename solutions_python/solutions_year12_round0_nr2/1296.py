#!/usr/bin/env python
# Marco Gallotta

T = int(raw_input())
for case in xrange(T):
  line = map(int, raw_input().split())
  N = line[0]
  S = line[1]
  p = line[2]
  t = line[3:]

  ans = 0
  for score in reversed(sorted(t)):
    if score >= 3*p-2:
      ans += 1
    elif p > 1 and score >= 3*p-4 and S:
      ans += 1
      S -= 1

  print 'Case #%d: %d' % (case+1, ans)
