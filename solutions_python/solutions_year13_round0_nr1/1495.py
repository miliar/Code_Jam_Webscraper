
def check(B, c, x, y, dx, dy):
  return all(B[y + i * dy][x + i * dx] in [ c, 'T' ] for i in range(4))

def checkWin(B, c):
  return any([
    any(check(B, c, x, 0, 0, 1) for x in range(4)),
    any(check(B, c, 0, y, 1, 0) for y in range(4)),
    check(B, c, 0, 0, 1, 1),
    check(B, c, 0, 3, 1, -1)
  ])

for t in range(int(input())):
  B = [ input() for y in range(4) ]
  print('Case #', t+1, ': ', sep='', end='')
  if checkWin(B, 'X'):
    print('X won')
  elif checkWin(B, 'O'):
    print('O won')
  elif any('.' in row for row in B):
    print('Game has not completed')
  else:
    print('Draw')
  input()
