def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

_T = readint()
for _t in range(_T):
  print 'Case #%i:'%(_t+1),

  N = readint()
  A = readarray(int)
  sA = [(a, i) for (i, a) in enumerate(A)]
  sA.sort()
  B = [i for (_, i) in sA]

  left = 0
  right = N-1
  
  res = 0
  for k in range(N):
    i = B[k]
    if i - left <= right - i:
      res += i - left
      left += 1
      for l in range(k+1, N):
        if B[l] < i:
          B[l] += 1
    else:
      res += right - i
      right -= 1
      for l in range(k+1, N):
        if B[l] > i:
          B[l] -= 1
  print res
