import sys

def solve(N, K):
#  print("Called with N=%i, K=%i" % (N, K))
  if K == N: return 0, 0
  if N % 2 == 0:
    LS = N/2 - 1
    RS = N/2
  else:
    LS = (N-1)/2
    RS = (N-1)/2
  if K == 1:
    return LS, RS
  else:
    Km = K - 1
    if Km % 2 == 0:
      if LS == RS: nextN = RS
      else: nextN = LS
      nextK = Km/2
    else:
      if LS == RS: nextN = LS
      else: nextN = RS
      nextK = (Km+1)/2
    return solve(nextN, nextK)

with open(sys.argv[1]) as f:
  T = int(f.readline())
  for t in range(T):
    N, K = tuple(map(int, f.readline().split()))
    LS, RS = solve(N, K)
    print("Case #%i: %i %i" % (t+1, max(LS,RS), min(LS,RS)))
