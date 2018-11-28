def process():
  direction = {'>':[0,1], '<':[0,-1], '^':[-1,0], 'v':[1,0]}
  R, C = map(int, raw_input().split())
  grid = [raw_input() for _ in xrange(R)]
  count = 0
  for i in xrange(R):
    for j in xrange(C):
      if grid[i][j] != '.':
        # Check Imp
        if grid[i].count('.') == C-1:
          col = 0
          for z in xrange(R):
            col += (grid[z][j] == '.')
          if col == R-1:
            return "IMPOSSIBLE"
        x, y = i, j
        found = False
        while x >= 0 and x < R and y >= 0 and y < C:
          x += direction[grid[i][j]][0]
          y += direction[grid[i][j]][1]
          if x >= 0 and x < R and y >= 0 and y < C and grid[x][y] != '.':
            found = True
            break
        if not found:
          count += 1
  return count

def main():
  tC = int(raw_input())
  tc = tC
  while tc > 0:
    tc -= 1
    ans = process()
    print u"Case #{}: {}".format(tC-tc, ans)

if __name__ == "__main__":
  main()
