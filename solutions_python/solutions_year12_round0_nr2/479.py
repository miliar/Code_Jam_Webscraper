N = int(raw_input())
for n in xrange(1,N+1):
  I = [int(x) for x in raw_input().split()]
  N, S, p, t = I[0], I[1], I[2], I[3:]
  if p == 0:
    print "Case #%d: %d" % (n, N)
    continue
  t1 = 3 * p - 2
  t2 = t1 - 2 if p > 1 else 1
  r, s = 0, 0
  for i in t:
    if i >= t1:
      r += 1
    elif s < S and i >= t2:
      r += 1
      s += 1
  print "Case #%d: %d" % (n, r)
