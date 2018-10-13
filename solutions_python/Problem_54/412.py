def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

C = int(raw_input())
for k in range(C):
  t = [int(s) for s in raw_input().split()]
  N = t[0]
  t = t[1:]
  T = abs(t[0] - t[1])
  for i in range(2, N):
    T = gcd(T, abs(t[i - 1] - t[i]))
  y = (T - t[0] % T) % T
  print 'Case #{0}: {1}'.format(k + 1, y)
