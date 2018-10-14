for case in xrange(1, int(raw_input())+1):
  N = int(raw_input())
  C = map(int, raw_input().split())
  xor_all = 0
  for c in C:
    xor_all ^= c

  if xor_all == 0:
    ans = sum(sorted(C)[1:])
  else:
    ans = None

  print "Case #%d: %s" % (case, str(ans) if ans is not None else "NO")
