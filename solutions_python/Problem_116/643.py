#!/usr/bin/python

#f = open('a_tictactoetomek_input.txt')
f = open('A-small-attempt0.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('a_result.txt', 'w')
def find_winning_row(list):
  #print list
  if '.' in list:
    return False
  elif 'X' in list and 'O' not in list:
    return True
  elif 'O' in list and 'X' not in list:
    return True
  else:
    return False

def find_winning_col(board):
  res = '.'
  inv_board = []
  for i in range (0,4):
    line = ""
    for j in range(0,4):
      line += board[j][i]
    if find_winning_row(line):
      if line[0]!='T':
        return line[0]
      else:
        return line[1]

  return res
def find_winning_diag(board):
  res = '.'
  diag1 = ""
  diag2 = ""
  for i in range (0,4):
    diag1 += board[i][i]
    diag2 += board[i][3-i]
  #print "diag1=",diag1
  #print "diag2=",diag2
  if find_winning_row(diag1):
    if diag1[0]!='T':
      return diag1[0]
    else:
      return diag1[1]
  elif find_winning_row(diag2):
    if diag2[0]!='T':
      return diag2[0]
    else:
      return diag2[1]
  else:
    return res

for i in range (0,numcase):
  board = []
  won = False
  not_complete = False
  for j in range(0,4):
    line = f.readline()
    if won is not True:
      won = find_winning_row(line)
      #print 'Result=',str(won)
    #assume complete unless the '.' is found later

      if won:
        winning_side = line[0]
    if '.' in line:
      not_complete = True
    board.append(line)
  if won:
    answ_sentence = "Case #"+str(i+1)+": "+ winning_side + " won"
  else:
    result = find_winning_col(board)
    #print 'col result =',result
    if result == '.':
      result = find_winning_diag(board)
    if result != '.':
      answ_sentence = "Case #"+str(i+1)+": "+ result + " won"
    elif not_complete:
      answ_sentence = "Case #"+str(i+1)+": "+ "Game has not completed"
    else:
      answ_sentence = "Case #"+str(i+1)+": "+ "Draw"
  
  fout.write(answ_sentence)
  fout.write('\n')
  print answ_sentence
  f.readline()
