
for case in range(1, int(input()) + 1):
  Y, X = map(int, input().split())
  tiles = [list(input()) for _ in range(Y)]
  print('Case #%d:' % case)

  def replace(y, x):
    for a, b in [(y, x), (y, x+1), (y+1, x), (y+1, x+1)]:
      if tiles[a][b] != '#':
        return False
      tiles[a][b] = '\\' if (a == y) ^ (b == x) else '/'
    return True

  possible = True
  for y, x in [(a, b) for a in range(Y) for b in range(X)]:
    if tiles[y][x] in './\\':
      continue

    if x == X-1 or y == Y-1 or tiles[y][x] == '#' and not replace(y, x):
      possible = False
      print('Impossible')
      break

  if possible:
    print('\n'.join(''.join(t) for t in tiles))
