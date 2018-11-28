def dp(P, M):
  if P == 1:
    if M[0] + M[1] > 0:
      return 1
    else:
      return 0
  else:
    if sum(M) > 0:
      mi = len(M) / 2
      M2 = []
      for i in M:
        if i > 0:
          M2.append(i - 1)
        else:
          M2.append(0)
      cost = 1 + dp(P - 1, M2[0:mi]) + dp(P - 1, M2[mi:len(M)])
      return cost
    else:
      return 0

T = int(raw_input())
for t in xrange(T):
  P = int(raw_input())
  M = [P - int(s) for s in raw_input().split()]
  prices = []
  for p in xrange(P):
    prices.append([int(s) for s in raw_input().split()])
  print 'Case #{0}: {1}'.format(t + 1, dp(P, M))
