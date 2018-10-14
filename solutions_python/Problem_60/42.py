INF = 10000000000000

for case in xrange(1, int(raw_input())+1):
  N, K, B, T = map(int, raw_input().split())
  X = map(int, raw_input().split())
  V = map(int, raw_input().split())
  ans = 0

  can_make = [float(B-X[i]) / V[i] < T + 0.000000001 for i in xrange(N)]
  k, front = 0, 0
  for i in xrange(N-1, -1, -1):
    if can_make[i] and k < K:
      k += 1
      ans += front
    else:
      front += 1

  if k < K:
    print "Case #%d: %s" % (case, "IMPOSSIBLE")
  else:
    print "Case #%d: %d" % (case, ans)
