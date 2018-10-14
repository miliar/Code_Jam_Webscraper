def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

_T = readint()
for _t in range(_T):
  print 'Case #%i:'%(_t+1),

  N, X = readarray(int)
  S = readarray(int)
  S.sort()

  i = 0
  j = N-1
  res = 0
  while i < j:
    if S[i]+S[j] <= X:
      res += 1
      i += 1
      j -= 1
    else:
      res += 1
      j -= 1
  if i == j:
    res += 1
  print res
