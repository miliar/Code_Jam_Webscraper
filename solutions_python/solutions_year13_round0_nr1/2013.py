#!/usr/bin/python
# coding: UTF-8

# T can be either X or O so replace it by both

def check_same(input_list):
  return input_list == [input_list[0]] * len(input_list)


def winner(input_list):
  winning_rows = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], 
                  [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
                  [0, 5, 10, 15], [3, 6, 9, 12]
                 ]
  for row in winning_rows:
    if check_same([input_list[i] for i in row]) and input_list[row[0]] != '.':
      return input_list[row[0]] + ' won' # return the Symbol of the player
  
  return 'none'

if __name__ == "__main__":
  #f = open('input-task-1.txt')
  #f_out = open('prob_1_out.txt', 'w')
  f = open('A-large.in')
  f_out = open('output_prob_1_large', 'w')
  T = int(f.readline()[:-1]) # of input cases
  
  for i in range(T):
    result = ''
    board_X = []
    board_O = []
    for j in range(4):
      line = f.readline()[:-1]
      for char in line:
        if char == 'T':
          board_X.append('X') # building the board
          board_O.append('O')
        else:
          board_X.append(char)
          board_O.append(char)
    
    #print board_X
    #print board_O
    result_X = winner(board_X)
    result_O = winner(board_O)
    if result_X != 'none': result = result_X
    elif result_O != 'none': result = result_O
    else:
      for char in board_X:
        if char == '.':
           result = 'Game has not completed'
      if result == '': result = 'Draw'
     
    f.readline()
    f_out.write("Case #" + str(i+1 )+ ": " + result + "\n")

