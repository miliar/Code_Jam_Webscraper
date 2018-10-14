from collections import deque
def solve(zi):
  n, m = map(int, input().split())
  origBoard = [['.' for i in range(n)] for j in range(n)]
  resBoard = [['.' for i in range(n)] for j in range(n)]
  H, V, Z, N = [False] * n, [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)

  for i in range(m):
    c, x, y = input().split()
    x, y = int(x)-1, int(y)-1
    origBoard[x][y] = c
    resBoard[x][y] = c
    if c == 'x' or c == 'o':
      H[x] = True
      V[y] = True
    if c == '+' or c == 'o':
      Z[x + y] = True
      N[(n-1-x) + y] = True

  for x in range(n):
    for y in range(n):
      if not H[x] and not V[y]:
        H[x], V[y] = True, True
        resBoard[x][y] = 'x' if resBoard[x][y] == '.' else 'o'

  tuples = [(x, y) for x in range(n) for y in range(n)]
  def cmpkey(tp):
    x, y = tp
    return min(x+y, (n-1-x)+y, x+(n-1-y), (n-1-x)+(n-1-y))
  tuples.sort(key = cmpkey)
  #print(tuples)

  for x, y in tuples:
    if not Z[x + y] and not N[(n-1-x) + y]:
      Z[x + y], N[(n-1-x) + y] = True, True
      resBoard[x][y] = '+' if resBoard[x][y] == '.' else 'o'

  #for i in range(n): print(resBoard[i])

  score, change = 0, []
  for x in range(n):
    for y in range(n):
      c = resBoard[x][y]
      if c == 'o': score += 2
      elif c == '+' or c == 'x': score += 1

      if origBoard[x][y] != c:
        change.append((c, x, y))

  print('Case #%d: %d %d'%(zi+1, score, len(change)))
  for c, x, y in change:
    print('%s %d %d'%(c, x+1, y+1))


zn = int(input())
for zi in range(zn):
  solve(zi)

