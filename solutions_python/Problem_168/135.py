def readint(): return int(raw_input())
def readlist(f): return map(f, raw_input().split())

dirs = {
  '^' : (-1, 0),
  'v' : (1, 0),
  '<' : (0, -1),
  '>' : (0, 1)
}

def ok(i, j, N, M):
  return i >= 0 and j >= 0 and i < N and j < M

def solve():
  N, M = readlist(int)
  G = []
  for i in range(N):
    G.append(raw_input())
  res = 0
  for i in range(N):
    for j in range(M):
      if G[i][j] == '.': continue
      di, dj = dirs[G[i][j]]
      # Check if already good
      ii, jj = i + di, j + dj
      while ok(ii, jj, N, M):
        if G[ii][jj] != '.': break
        ii += di
        jj += dj
      if ok(ii, jj, N, M): continue
      # Not good...
      res += 1
      # Check if doable
      for di, dj in dirs.values():
        ii, jj = i + di, j + dj
        while ok(ii, jj, N, M):
          if G[ii][jj] != '.': break
          ii += di
          jj += dj
        if ok(ii, jj, N, M): break
      else:
        return 'IMPOSSIBLE'
  return res

T = readint()
for t in range(T):
  print 'Case #{}: {}'.format(t+1, solve())
