def good(i, j, n, m):
  return i < n and j < m and i >=0 and j >= 0

f = open('a.in', 'r')
T = int(f.readline())
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for tno in range(T):
  n, m = [ int(x) for x in f.readline().split(' ') ]
  A = [ [int(x) for x in f.readline().split(' ')] for y in range(n) ]
  B = [ [0] * m for x in range(n)]
  c = chr(ord('a') - 1)
  for i in range(n):
    for j in range(m):
      if B[i][j] != 0:
        continue
      ii, jj = i, j
      pos = []
      while B[ii][jj] == 0:
        nx, ny = 0, 0
        for (xx, yy) in dirs:
          if good(xx + ii, yy + jj, n, m) and A[xx + ii][yy + jj] < \
              A[nx + ii][ny + jj]:
            nx = xx
            ny = yy
        if nx + ny == 0:
          break
        pos.append((ii, jj))
        ii += nx
        jj += ny
      if B[ii][jj] == 0:
        c = chr(ord(c) + 1)
        col = c
        B[ii][jj] = col
      else:
        col = B[ii][jj]
      for (ii, jj) in pos:
        B[ii][jj] = col
  print 'Case #%s:' % (tno + 1)
  for row in B:
    print ' '.join(row)
