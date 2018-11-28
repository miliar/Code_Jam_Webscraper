for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  N, V, X = map(float, raw_input().split())
  N = int(N)
  R = []
  C = []
  for _ in xrange(N):
    r, c = map(float, raw_input().split())
    R.append(r)
    C.append(c)
  if N == 2 and C[0] == C[1]: # equivalent to one
    N = 1
    R[0] += R[1]
  if N == 1:
    if C[0] != X:
      print "IMPOSSIBLE"
    else:
      print "%.10f" % (V / R[0])
  else:
    assert N == 2
    a = (X-C[1])/(C[0]-C[1])
    if 0 <= a <= 1:
      v1 = V*a
      v2 = V*(1-a)
      print "%.14f" % max(v1/R[0], v2/R[1])
    else:
      print "IMPOSSIBLE"
