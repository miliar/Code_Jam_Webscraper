import os

def read_games(lines):
  """Read all games from lines """
  game_count = int(lines[0])
  game_lines = lines[1:]
  for game in range(game_count):
    yield [game_lines[i].strip() for i in range(5 * game, 5 * game + 4)]

def get_in(game, coord):
  x, y = coord
  if x < 4 and y < 4:
    return game[y][x]

def get_coords(game, coords):
  return [get_in(game, c) for c in coords]

def column(v):
  return [(i, v) for i in range(4)]

def row(h):
  return [(h, i) for i in range(4)]

def diag_top_left():
  return [(i, i) for i in range(4)]

def diag_bottom_left():
  return [(3-i, i) for i in range(4)]

def check_winner(values, player):
  return all(map(lambda x: x in (player, 'T'), values))

def check_game(game):
  for player in ('X', 'O'):
    for i in range(4):
      if check_winner(get_coords(game, row(i)), player):
        return player
      if check_winner(get_coords(game, column(i)), player):
        return player
    if check_winner(get_coords(game, diag_top_left()), player):
      return player
    if check_winner(get_coords(game, diag_bottom_left()), player):
      return player
  if any(map(lambda r: '.' in r, game)):
    return '.'
  return 'D'

def format_result(game_result):
  return {'X': 'X won',
          'O': 'O won',
          'D': 'Draw',
          '.': 'Game has not completed'}[game_result]

# ran in interactive python shell via
# import tttt
# tttt.main('A-large.in')
def main(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
  with open(filename + '.out', 'w') as out:
    games = read_games(lines)
    counter = 1
    for game in games:
      print >> out, ("Case #%d: %s" % (counter, format_result(check_game(game))))
      counter += 1
