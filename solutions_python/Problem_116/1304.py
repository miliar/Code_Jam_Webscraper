import csv

def getcol(game,n):
  col = []
  for i in xrange(4):
    col.append(game[i][n])
  return col

def getdiag(game, n):
  diag= []
  add = (-1)**n
  for i in xrange(4):
    diag.append(game[i][3*n + i*add])
  return diag

def isWin(row):
  score = 0
  for i in xrange(4):
    score += ord(row[i])
  if score == 348 or score == 352:
    return "X won"
  elif score == 321 or score == 316:
    return "O won"
  else:
    return False

def evalGame(game):
  for i in xrange(4):
    row = game[i]
    test = isWin(row)
    if test:
      return test
  for i in xrange(4):
    col = getcol(game,i)
    test = isWin(col)
    if test:
      return test
  for i in xrange(2):
    diag = getdiag(game,i)
    test = isWin(diag)
    if test:
      return test
  for i in xrange(4):
    if '.' in game[i]:
      return 'Game has not completed'
  return 'Draw'



if __name__ == "__main__":

  f = csv.reader(open('A-large.in','r'), delimiter = ' ')
  out = open("A-large.out","w")

  T = int(f.next()[0])

  for case in xrange(1,T+1):
    game = []
    for i in xrange(4):
      game.append([x for x in f.next()[0]])
    f.next()
    result = evalGame(game)
    out.write("Case #%d: %s\n" % (case, result))

  out.close()
