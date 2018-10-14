import sys

n = int(sys.stdin.readline())


board = []
for i in range(n):
  b = []
  b.append(sys.stdin.readline())
  b.append(sys.stdin.readline())
  b.append(sys.stdin.readline())
  b.append(sys.stdin.readline())
  board.append(b)
  sys.stdin.readline()



def process_board(b, boar):
  for winner in 'X','O':
    for i in range(4):
      line_total = 0
      for j in range(4):
        if winner == boar[i][j] or 'T' == boar[i][j]:
          line_total += 1
      if line_total == 4:
        print 'Case #'+str(b+1)+': '+winner +' won'
        return
    for j in range(4):
      line_total = 0
      for i in range(4):
        if winner == boar[i][j] or 'T' == boar[i][j]:
          line_total += 1
      if line_total == 4:
        print 'Case #'+str(b+1)+': '+winner +' won'
        return
    line_total = 0
    for i in range(4):
      if winner == boar[i][i] or 'T' == boar[i][i]:
        line_total += 1
    if line_total == 4:
      print 'Case #'+str(b+1)+': '+winner +' won'
      return
    line_total = 0
    for i in range(4):
      if winner == boar[3-i][i] or 'T' == boar[3-i][i]:
        line_total += 1
    if line_total == 4:
      print 'Case #'+str(b+1)+': '+winner +' won'
      return
  if '.' in boar[0] or '.' in boar[1] or '.' in boar[2] or '.' in boar[3]:
    print 'Case #'+str(b+1)+': Game has not completed'
  else:
    print 'Case #'+str(b+1)+': Draw'  


for b in range(len(board)):
  boar = board[b]
  process_board(b, boar)
