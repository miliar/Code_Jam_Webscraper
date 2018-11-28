from os import sys

def flip(s):
  return "".join(["-" if c == "+" else "+" for c in s])

def solve(S, K):
  l = len(S)
  leftmost_sad = S.find("-")
  flips = 0
  while leftmost_sad <= l-K and leftmost_sad != -1:
    S = S[:leftmost_sad] + flip(S[leftmost_sad:leftmost_sad+K]) + S[leftmost_sad+K:]
    flips += 1
    leftmost_sad = S.find("-")

  if S.find("-") == -1:
    return flips
  else:
    return "IMPOSSIBLE"

num_cases = int(sys.stdin.readline())

for case in range(1,num_cases+1):
  S, K = sys.stdin.readline().split()
  K = int(K)
  print "Case #" + str(case) + ":", solve(S, K)
