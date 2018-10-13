#!/usr/bin/python
import sys, os, numpy as np

def print_usage():
  print "Usage: tic_tac_toe_tomek.py <file>"

  
def who_won(game):
  """
  Returns:
  0 = unfinished
  1 = player 1
  2 = player 2
  3 = draw 

  """

  rows,cols = np.shape(game)
  num_to_win = 4
  # Horizontal?
  num_blank = 0
  for i in range(rows):
    votes = {}
    for j in range(cols):
      if game[i,j] == 0:
        num_blank += 1
      if game[i,j] not in votes:
        votes[game[i,j]] = 1
      else:
        votes[game[i,j]] += 1

    num_1s = 0 if 1.0 not in votes else votes[1.0]
    num_2s = 0 if 2.0 not in votes else votes[2.0]
    num_ts = 0 if 3.0 not in votes else votes[3.0]

    if num_1s + num_ts == 4 and num_2s + num_ts < 4:
      return "X won"
    elif num_2s + num_ts == 4 and num_1s + num_ts < 4:
      return "O won"
    elif num_1s + num_ts == num_2s + num_ts and num_1s + num_ts == 4:
      return "Draw"

  for j in range(cols):
    votes = {}
    for i in range(rows):
      if game[i,j] not in votes:
        votes[game[i,j]] = 1
      else:
        votes[game[i,j]] += 1
    num_1s = 0 if 1.0 not in votes else votes[1.0]
    num_2s = 0 if 2.0 not in votes else votes[2.0]
    num_ts = 0 if 3.0 not in votes else votes[3.0]
    if num_1s + num_ts == 4 and num_2s + num_ts < 4:
      return "X won"
    elif num_2s + num_ts == 4 and num_1s + num_ts < 4:
      return "O won"
    elif num_1s + num_ts == num_2s + num_ts and num_1s + num_ts == 4:
      return "Draw"

  # Check top-left to bottom-right diagonal
  votes = {}
  for i in range(rows):
    if game[i,i] not in votes:
      votes[game[i,i]] = 1
    else:
      votes[game[i,i]] += 1
    num_1s = 0 if 1.0 not in votes else votes[1.0]
    num_2s = 0 if 2.0 not in votes else votes[2.0]
    num_ts = 0 if 3.0 not in votes else votes[3.0]

  if num_1s + num_ts == 4 and num_2s + num_ts < 4:
    return "X won"
  elif num_2s + num_ts == 4 and num_1s + num_ts < 4:
    return "O won"
  elif num_1s + num_ts == num_2s + num_ts and num_1s + num_ts == 4:
    return "Draw"


  # Check top-right to bottom-left diagonal
  votes = {}
  for i in range(rows):
    if game[i,3-i] not in votes:
      votes[game[i,3-i]] = 1
    else:
      votes[game[i,3-i]] += 1
    num_1s = 0 if 1.0 not in votes else votes[1.0]
    num_2s = 0 if 2.0 not in votes else votes[2.0]
    num_ts = 0 if 3.0 not in votes else votes[3.0]

  if num_1s + num_ts == 4 and num_2s + num_ts < 4:
    return "X won"
  elif num_2s + num_ts == 4 and num_1s + num_ts < 4:
    return "O won"
  elif num_1s + num_ts == num_2s + num_ts and num_1s + num_ts == 4:
    return "Draw"
    
  if num_blank == 0:
    return "Draw"
  return "Game has not completed"
    

def convert_game_string_to_numpy_array(game_string):
  game_rows = game_string.split("\n")
  shape = (len(game_rows), len(game_rows[0]))
  shape = (4,4)
  game_mat = np.zeros(shape)
  for i in range(4):
    game_row = game_rows[i]
    vals = []
    for char in game_row:
      if char == 'X':
        vals.append(1)
      elif char == 'O':
        vals.append(2)
      elif char == 'T':
        vals.append(3)
      elif char == '.':
        vals.append(0)
    if len(vals) > 0:
      game_mat[i,:] = np.array(vals)
  rows, cols = np.shape(game_mat)
  if rows == 5:
    print 'game string: \n', game_string
    print game_mat
  return game_mat
    
def read_data(filename):
  with open(filename) as data_file:
    data = data_file.read()

  
  num_games = data.split("\n")[0]
  data = "\n".join(data.split("\n")[1:])
  games = data.split("\n\n")

  games_list = []
  for game in games:
    if game == "":
      continue
    games_list.append(convert_game_string_to_numpy_array(game))

  return games_list



def main():
  if len(sys.argv) != 2:
    print_usage()
    sys.exit(1)
  
  filename = os.path.abspath(sys.argv[1])
  games = read_data(filename)

  for i in range(len(games)):
    print 'Case #' + str(i+1) + ': ' + who_won(games[i])


if __name__ == "__main__":
  main()
