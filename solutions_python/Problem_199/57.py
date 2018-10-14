N = int(input())
for n in range(N):
  inp = input().split()
  S = inp[0]
  K = int(inp[1])
  S2 = [False] * (len(S) + 1)
  S2[0] = "+" != S[0]
  for i in range(1, len(S)):
    S2[i] = S[i-1] != S[i]
  S2[-1] = S[-1] != "+"
  flips = 0
  for i in range(len(S2) - K):
    if S2[i]:
      S2[i + K] = not S2[i + K]
      flips += 1
  resp = "IMPOSSIBLE" if any(S2[-K:]) else flips
  print("Case #{}: {}".format(n+1, resp))
    
