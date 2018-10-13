_T = int(raw_input())
for _t in range(1, _T+1):
  N, M = map(int, raw_input().split())
  G = [[[0] * N for _ in range(N)] for __ in range(2)]

  score = 0
  for _ in range(M):
    m, i, j = raw_input().split()
    i = int(i)-1
    j = int(j)-1
    if m == '+' or m == 'o':
      G[0][i][j] = 1
      score += 1
    if m == 'x' or m == 'o':
      G[1][i][j] = 1
      score += 1

# In G[0]: no two 1s on same diagonal
# In G[1]: no two 1s on same row/column
  
  C = dict()

# Fill G[1]:
  row_done = [False]*N
  col_done = [False]*N
  for i in range(N):
    for j in range(N):
      if G[1][i][j] == 1:
        row_done[i] = True
        col_done[j] = True
  i, j = 0, 0
  while i < N and j < N:
    if row_done[i]:
      i += 1
      continue
    if col_done[j]:
      j += 1
      continue
    if G[0][i][j] == 1:
      C[i, j] = 'o'
    else:
      C[i, j] = 'x'
    row_done[i] = True
    col_done[j] = True
    G[1][i][j] = 1
    score += 1

# Fill G[0]:
  def check(ii, jj):
    for i in range(N):
      for j in range(N):
        if G[0][i][j] == 1 and (i + j == ii + jj or i - j == ii - jj):
          return False
    return True
  
  def add_change(i, j):
    if G[1][i][j] == 1:
      C[i, j] = 'o'
    else:
      C[i, j] = '+'

  def do(i, j):
    global score
    if check(i, j):
      add_change(i, j)
      G[0][i][j] = 1
      score += 1

  corners = (
    (0, 0, 1, 1),
    (0, N-1, 1, -1),
    (N-1, 0, -1, 1),
    (N-1, N-1, -1, -1)
  )
  for d in range(N):
    for (i, j, di, dj) in corners:
      do(i + di*d, j)
      do(i, j + dj*d)

  print 'Case #{}: {} {}'.format(_t, score, len(C))
  for (i, j) in C:
    print '{} {} {}'.format(C[i, j], i+1, j+1)
