tn = input()
ti = 0

while ti < tn:
  d, n = map(int, raw_input().split())
  t = 0

  while n > 0:
    n -= 1
    k, s = map(int, raw_input().split())
    t = max(t, 1.0 * (d - k) / s)

  f = 1.0 * d / t

  ti += 1
  print 'Case #%s: %s' % (ti, f)
