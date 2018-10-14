T = int(raw_input())

def solve(N, M):
  grass = [[0 for j in range(M)] for i in range(N)]
  mnline = [0 for i in range(N)]
  mxline = [0 for i in range(N)]
  mncol = [0 for i in range(M)]
  mxcol = [0 for i in range(M)]
  for i in range(N):
    grass[i] = map(int,raw_input().split())
    mnline[i] = min(grass[i])
    mxline[i] = max(grass[i])
  for j in range(M):
    col = [grass[i][j] for i in range(N)]
    mncol[j] = min(col)
    mxcol[j] = max(col)
  for i in range(N):
    for j in range(M):
      if mxcol[j] != mncol[j] and mxline[i] != mnline[i]:
        if grass[i][j] != mxcol[j] and grass[i][j] != mxline[i]:
          return "NO"
  return "YES"

for case in range(1,T+1):
  N, M = map(int,raw_input().split())
  
  print 'Case #' + str(case) + ': ' + solve(N, M) 