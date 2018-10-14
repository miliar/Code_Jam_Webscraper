from sys import stdin

T = int(stdin.readline())

for tc in xrange(1, T+1):
  S, shyness = stdin.readline().strip().split()
  S = int(S)
  count = 0
  extra = 0
  for i, c in enumerate(shyness):
    x = int(c)
    if x:
      extra += max(0, i - (count + extra))
    count += x
  print "Case #%d: %d" % (tc, extra)
