def check(S,K):
  if len(S) == 0:
    return 0
  elif S[0] == '+':
    idx = S.find('-')
    if idx == -1:
      return 0
    else:
      return check(S[idx:],K) 
  else: # S[0] == '-'
    if len(S) < K:
      return 'IMPOSSIBLE'
    else:
      S1 = ''.join(['+' if a == '-' else '-' for a in S[:K]])
      S2 = S[K:]
      ans = check(S1+S2,K)
      if ans == 'IMPOSSIBLE':
        return ans
      else:
        return (1+ans)

T = int(input())
for i in range(1,T+1):
  data = input().split(' ')
  S = data[0]
  K = int(data[1])
  ans = str(check(S,K))
  print('Case #{}: {}'.format(i,ans))

