def flip(S):
  fliped = ''
  for i in S:
    fliped += '+' if i == '-' else '-'
  return fliped

def Solve(S,K):
  c = 0
  nIndex = S.find('-')
  while (nIndex != -1):
    #try:
    #print S
    substring = S[nIndex:nIndex+K]
    #print 'sub',substring
    if len(substring) < K:
      return 'IMPOSSIBLE'
    #except IndexError:
     # return 'IMPOSSIBLE'
    substring = flip(substring)
    #print 'fliped',substring
    S = S[:nIndex] + substring + S[nIndex+K:]
    #print S
    c = c + 1
    nIndex = S.find('-')
  return c
    
T = int(input())  
for i in range(1, T + 1):
  S, K = [s for s in raw_input().split(" ")]
  print("Case #{}: {}".format(i, Solve(S,int(K))))




