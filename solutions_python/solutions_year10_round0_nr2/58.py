T = int(raw_input())

def gcd(a, b):
  while b:
    a %= b
    a, b = b, a
  return a

for t in range(T):
  x = map(int, raw_input().split())
  N = x[0]
  g = 0
  for i in range(N-1):
    g = gcd(g, abs(x[i+1]-x[i+2]))
  print "Case #%d: %d" % (t+1, (g - (x[1]%g)) % g)
