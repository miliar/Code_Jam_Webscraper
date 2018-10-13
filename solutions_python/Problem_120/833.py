import math

def paint(r):
  return 2 * r + 1

T = int(raw_input())
for case in range(1, T+1):
  s = raw_input().split(' ')
  r = int(s[0])
  t = int(s[1])
  circle = 0
  while (t > 0):
    p = paint(r)
    if (t - p >= 0):
      circle = circle + 1
    t = t - p
    r = r + 2
  print 'Case #{0}: {1}'.format(case, circle)
