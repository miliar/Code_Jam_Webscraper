import sys
import numpy as np

def readint(f):
  return int(f.readline())

def check_winner(tup, game_num):
  x_wins = True
  o_wins = True
  over = True
  for x in tup:
    if x == 1:
      x_wins = False
    elif x == 0:
      o_wins = False
    elif x == 3:
      x_wins = False
      o_wins = False
      over = False
  if x_wins:
    print 'Case #%d: X won' % game_num
  elif o_wins:
    print 'Case #%d: O won' % game_num
  return (x_wins or o_wins, over)

def interpret(c):
  if c == 'X':
    return 0
  elif c == 'O':
    return 1
  elif c == 'T':
    return 2
  elif c == '.':
    return 3
  else:
    assert(False)

def readgame(f):
  game = np.zeros((4,4))
  for y in xrange(4):
    for x, c in enumerate(f.readline().strip()):
      game[x,y] = interpret(c)
  f.readline()
  return game

with open(sys.argv[1], 'r') as f:
  ncases = readint(f)
  for i in xrange(ncases):
    over = True
    won = False
    game = readgame(f)
    ended = True
    # print game
    # Check rows for winner
    for row in xrange(game.shape[0]):
      won, ov = check_winner(game[row], i+1)
      if won:
        break
      over = over and ov
    if won:
      continue

    # Check columns for winner
    for col in xrange(game.shape[1]):
      won, ov = check_winner(game[:, col], i+1)
      if won:
        break
      over = over and ov
    if won:
      continue

    # Check diagonals for winner
    l = []
    for x in xrange(game.shape[0]):
      l.append(game[x][x])
    won, ov = check_winner(l, i+1)
    if won:
      continue
    over = over and ov

    l = []
    for x in xrange(game.shape[0]):
      l.append(game[game.shape[0] - 1 - x][x])
    won, ov = check_winner(l, i+1)
    if won:
      continue
    over = over and ov

    if over:
      print 'Case #%d: Draw' % (i+1)
    else:
      print 'Case #%d: Game has not completed' % (i+1)
