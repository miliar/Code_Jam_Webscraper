import sys

def istidy(N):
  s = str(N)
  for i in range(len(s)-1):
    if s[i] > s[i+1]:
      return False
  return True

def solve_small(N):
  x = N
  while x >= 1:
    if istidy(x): return x
    x -= 1

def solve_large(N):
  S = [int(x) for x in str(N)]
  sol = [-1]*len(S)
  for i in range(len(S)-1, -1, -1):
    if i == 0:
      sol[i] = S[0]
      break
    d = S[i]
    if d >= S[i-1]:
      sol[i] = d
    else:
      for j in range(i,len(S)):
        sol[j] = 9
      S[i-1] -= 1
  return int("".join(map(str, sol)))

with open(sys.argv[1]) as f:
  T = int(f.readline())
  for t in range(T):
    N  = int(f.readline())
    sol = solve_large(N)
    print("Case #%i: %i" % (t+1, sol))
