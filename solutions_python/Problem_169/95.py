T = int(raw_input())
for t in range(1, T+1):
  tokens = raw_input().split()
  N = int(tokens[0])
  V,X = map(float, tokens[1:])
  cold = []
  warm = []
  middle = []
  for i in range(N):
    R,C = map(float, raw_input().split())
    if C < X:
      cold.append((C,R))
    elif C > X:
      warm.append((C,R))
    else:
      middle.append((C,R))
  warm.sort()
  cold.sort()
  R1 = 0
  C1 = 0
  res = float("inf")
  if middle:
    R = 0
    for m in middle:
      R += m[1]
    res = V / R
  for w in warm:
    C1 = (R1*C1 + w[1]*w[0]) / (R1 + w[1])
    R1 += w[1]
    R2 = 0
    C2 = 0
    for c in cold:
      C2 = (R2*C2 + c[1]*c[0]) / (R2 + c[1])
      R2 += c[1]
      V1 = V*(X-C2) / (C1 - C2)
      V2 = V - V1
      t1 = V1 / R1
      t2 = V2 / R2
      res = min(res, max(t1,t2))
  print "Case #%d: %s" % (t, "IMPOSSIBLE" if res == float("inf") else str(res))
