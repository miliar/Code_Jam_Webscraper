
import sys
import re

def get_game(games):
  game = []
  for i in range(5):
    line = games.pop(0)
    if i > 0:
      game.append(line)
  return game

def get_winner(line):
  if re.search('[XT]{4}', line):
    return True, 'X won'
  elif re.search('[OT]{4}', line):
    return True, 'O won'
  elif re.search('\.', line):
    return False, '.'
  else:
    return False, None
  
def get_result(game):
  has_empty, has_win = False, False
  cols, diags = ['','','',''], ['','']
  i = 0
  # check rows, make columns and diagonals
  for line in game:
    row_result = get_winner(line)
    if row_result[0]:
      return row_result[1]
    if row_result[1]:
      has_empty = True
    cols[0], cols[1], cols[2], cols[3] = cols[0] + line[0], cols[1] + line[1], cols[2] + line[2], cols[3] + line[3]
    diags[0], diags[1] = diags[0] + line[i], diags[1] + line[3 - i]
    i += 1
  # check columns
  for col in cols:
    col_result = get_winner(col)
    if col_result[0]:
      return col_result[1]
  # check diagonals
  for diag in diags:
    diag_result = get_winner(diag)
    if diag_result[0]:
      return diag_result[1]
  # at this point, no winner
  if has_empty:
    return 'Game has not completed'
  return 'Draw'
  
def main():
  input = open(sys.argv[1], 'r') # read only
  # will need input.readlines(), input.read(), or something similar later, which will separate lines into
  # list elements, leaving the \n attached to the end of each line
  # the string method .rstrip('\n') will remove these
  output = open(sys.argv[2] + '.out', 'w') # write new file
  # will use output.write(result + '\n') later to write one 'result' line at a time to the output file
  games = input.readlines()
  games.pop()
  input.close()
  case = 1
  while games:
    game = get_game(games)
    output_line = 'Case #{}: {}'.format(case, get_result(game))
    output.write(output_line + '\n')
    case += 1
  # at end, close files to prevent any strange behavior due to file being left open after program closes
  output.close()
  print 'Done!'
  
if __name__ == '__main__':
  main()