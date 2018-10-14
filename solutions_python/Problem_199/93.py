_T = int(raw_input())
for _t in range(1, _T+1):
  S, K = raw_input().split()
  S = list(S)
  K = int(K)
  N = len(S)
  
  res = 0
  for i in range(N + 1 - K):
    if S[i] == '+': continue
    res += 1
    for j in range(i, i + K):
      if S[j] == '-':
        S[j] = '+'
      else:
        S[j] = '-'

  for i in range(N):
    if S[i] != '+':
      res = 'IMPOSSIBLE'
      break

  print 'Case #{}: {}'.format(_t, res)
