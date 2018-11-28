import sys

def flip_at(S, i, K):
  for j in range(i,i+K):
    S[j] *= -1

def solve(S, K):
  flips = 0
  for i in range(len(S)-K+1):
    if S[i] == -1:
      flip_at(S, i, K)
      flips += 1
  if S.count(+1) == len(S):
    return flips
  else:
    return "IMPOSSIBLE"

with open(sys.argv[1]) as f:
  T = int(f.readline())
  for t in range(T):
    line = f.readline().split()
    S = [+1 if x == "+" else -1 for x in line[0]]
    K = int(line[1])
    sol = solve(S, K)
    print("Case #%i: %s" % (t+1, sol))
