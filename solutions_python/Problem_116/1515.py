def iswin(string):
  if '.' in string:
    return ''
  n = string.count('X')
  char = 'X'
  if n == 0:
    n = string.count('O')
    char = 'O' 
  if n == 4 or (n == 3 and 'T' in string):
    return char
  return 'full'


numGames = input()
for case in xrange(1, numGames+1):
  game = []
  for i in xrange(4):
    game.append(raw_input())

  win = []
  ddr = ''  # diagonal down right: \
  ddl = ''  # diagonal down left:  /
  for i in xrange(4):
    # horizontal & vertical
    col = ''
    row = ''
    for j in xrange(4):
      col += game[j][i]
      row += game[i][j]

    rowwin = iswin(row)
    if rowwin != '':
      win.append(rowwin)
    colwin = iswin(col)
    if colwin != '':
      win.append(colwin)

    # diagonals
    ddr += game[i][i]
    ddl += game[i][3-i]
  ddrwin = iswin(ddr)
  if ddrwin != '':
    win.append(ddrwin)
  ddlwin = iswin(ddl)
  if ddlwin != '':
    win.append(ddlwin)

  print 'Case #{0}:'.format(case),
  if 'X' in win:
    if 'O' in win:
      print 'Draw'
    else:
      print 'X won'
  elif 'O' in win:
    print 'O won'
  else:
    if win.count('full') == 10:
      print 'Draw'
    else:
      print 'Game has not completed'

  raw_input()
