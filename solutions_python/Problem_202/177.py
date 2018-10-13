import sys

fin = sys.stdin

def main():
  num_cases = int(fin.readline().strip())
  for i in range(num_cases):
    case_num = i + 1
    output = solve()
    print('Case #%d: %s' % (case_num, output))

def solve():
  n, m = [int(x) for x in fin.readline().strip().split()]

  xs = [1] * n
  ys = [1] * n
  ps = [1] * (2 * n - 1)
  ms = [1] * (2 * n - 1)
  new_coords = []
  grid = [['.'] * n for i in range(n)]
  score = 0

  # Read input
  for i in range(m):
    symbol, x, y = fin.readline().strip().split()
    x = int(x) - 1
    y = int(y) - 1

    grid[x][y] = symbol

    if symbol == 'o' or symbol == 'x':
      score += 1
      xs[x] -= 1
      ys[y] -= 1


    if symbol == 'o' or symbol == '+':
      score += 1
      ps[x + y] -= 1
      ms[x - y] -= 1

  # Try to place +s. Try (0, i) and (n-1, i) for each i
  for y in range(n):
    for x in [0, n - 1]:
      if ps[x + y] and ms[x - y]:
        # place!
        score += 1
        ps[x + y] -= 1
        ms[x - y] -= 1
        new_coords.append((x, y, '+'))

  # Try to place xs, Try all coordinates!
  for x in range(n):
    for y in range(n):
      if xs[x] and ys[y]:
        # place!
        score += 1
        xs[x] -= 1
        ys[y] -= 1
        new_coords.append((x, y, 'x'))

  # Consolidate
  new_coords.sort()
  new_new_coords = {}
  for x, y, symbol in new_coords:
    if grid[x][y] == '.':
      new_new_coords[(x, y)] = symbol
      grid[x][y] = symbol
    elif grid[x][y] in ['x', '+']:
      new_new_coords[(x, y)] = 'o'
      grid[x][y] = 'o'
    else:
      raise ValueError('blah')

  result = ['%d %d' % (score, len(new_new_coords))]
  for (x, y), symbol in new_new_coords.iteritems():
    result.append('%s %d %d' % (symbol, x + 1, y + 1))

  return '\n'.join(result)

if __name__ == '__main__':
  main()
