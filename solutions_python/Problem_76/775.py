T = int (raw_input())
for t in xrange(1, T+1):
  N = int (raw_input())
  a = raw_input().split()
  a = [int(x) for x in a]
  xor = 0
  for x in a:
    xor ^= x
  if xor == 0:
    print "Case #%d: %d" % (t, sum(a) - min(a))
  else:
    print "Case #%d: NO" % t
