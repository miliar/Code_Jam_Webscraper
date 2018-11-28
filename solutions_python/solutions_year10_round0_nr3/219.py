T = int(raw_input())
for i in range(T):
  R, k, N = [int(s) for s in raw_input().split()]
  g = [int(s) for s in raw_input().split()]
  M = 0
  first = 0
  for t in range(R):
    m = 0
    last = 0
    for j in range(N):
      next = (first + j) % N
      if m + g[next] <= k:
        m += g[next]
        last = next
      else:
        break
    first = (last + 1) % N
    M += m
  print 'Case #{0}: {1}'.format(i + 1, M)
