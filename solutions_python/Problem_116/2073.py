# Function to get each test case.
def get_board(f):
  board = []
  for i in xrange(4):
    board.append(f.readline())
  return board

# Function to determine who won
def get_winner(board):

  def check_rows(board, player):
    valid = (player, 'T')
    for y in xrange(4):
      score = 0
      for x in xrange(4):
        if board[y][x] in valid:
          score += 1
        else:
          continue
        if score == 4:
          return player
    return ''

  def check_cols(board, player):
    valid = (player, 'T')
    for x in xrange(4):
      score = 0
      for y in xrange(4):
        if board[y][x] in valid:
          score += 1
        else:
          continue
        if score == 4:
          return player
    return ''

  def check_diags(board, player):
    valid = (player, 'T')
    score = 0
    for i in xrange(4):
      if board[i][i] in valid:
        score += 1
      else:
        break
      if score == 4:
        return player
    score = 0
    for i in xrange(4):
      if board[3 - i][i] in valid:
        score += 1
      else:
        break
      if score == 4:
        return player
    return ''

  winner = ''
  for player in ('X', 'O'):
    winner = winner or check_rows(board, player)
    winner = winner or check_cols(board, player)
    winner = winner or check_diags(board, player)
  return winner

f = open('A-large.in')

test_cases = int(f.readline())
results = []

for i in xrange(test_cases):
  board = get_board(f)
  w = get_winner(board)
  if w:
    results.append('%s won' % w)
  else:
    for line in board:
      if '.' in line:
        results.append('Game has not completed')
        break
    else:
      results.append('Draw')
  f.readline()

for i in xrange(len(results)):
  print 'Case #%d: %s' % (i + 1, results[i])