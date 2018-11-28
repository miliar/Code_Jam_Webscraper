import math

from math import sqrt

def game_checkrowcol(countrow, countcol):
  for x in countrow:
    if x == 4:
      return True
  for y in countcol:
    if y == 4:
      return True
  return False

def print_tic_tac(case, board, o):
  #Check if X or O won
  #Check if game board is full
    #if yes, Draw
    #if no, Game not completed
  
  result = 'asdf' 
  over = False
  blanks = 0
  rowX = [0,0,0,0]
  rowO = [0,0,0,0]
  colX = [0,0,0,0]
  colO = [0,0,0,0]
  
  r = 0
  for rowitem in board:
    colnum = 0
    for colval in rowitem[0]:
      if colval == 'X':
        rowX[r] += 1
        colX[colnum] += 1
      elif colval == 'O':
        rowO[r] += 1
        colO[colnum] += 1
      elif colval == 'T':
        rowX[r] += 1
        colX[colnum] += 1
        rowO[r] += 1
        colO[colnum] += 1
      else:
        blanks += 1
      colnum += 1
    r += 1
  
  for x in board:
    print x
  print rowX
  print colX
  print rowO
  print colO
  
  if game_checkrowcol(rowX, colX):
    over = True
    result = 'X won'
    print result
  elif game_checkrowcol(rowO, colO):
    over = True
    result = 'O won'
    print result
  else:
    #check diags for a win
    #diag 1 top left to bot right
    DiagXcount = 0
    DiagOcount = 0
    for col in range(0,4):
      row = 0
      for rowitem in board:
        if col == row: 
          if (rowitem[0][col] == 'X' or rowitem[0][col] == 'T'):
            DiagXcount += 1
          elif (rowitem[0][col] == 'O' or rowitem[0][col] == 'T'):
            DiagOcount += 1
          #print rowitem[0][col]
        row += 1
    if (DiagXcount == 4):
      over = True
      result = 'X won'
      print result
    elif (DiagOcount == 4):
      over = True
      result = 'O won'
      print result
    
    #diag 2 top right to bot left
    DiagXcount = 0
    DiagOcount = 0
    for col in range(3,-1,-1):
      row = 3
      for rowitem in board:
        print str(col) + str(row)
        if col == row: 
          if (rowitem[0][col] == 'X' or rowitem[0][col] == 'T'):
            DiagXcount += 1
          if (rowitem[0][col] == 'O' or rowitem[0][col] == 'T'):
            DiagOcount += 1
          print rowitem[0][col]
        row -= 1
    print DiagXcount
    print DiagOcount
    if (DiagXcount == 4):
      over = True
      result = 'X won'
      print result
    elif (DiagOcount == 4):
      over = True
      result = 'O won'
      print result
    
    
    
    #Noone won
    if(not over):
      if blanks > 0:
        result = 'Game has not completed'
      else:
        result = 'Draw'
  
  #write out end
  output = 'Case #' + str(case) + ': ' + result + '\n'
  print output
  o.write(output)

f = open('tictac.in')
o = open('tictac.out','r+')
num_cases = int(f.readline()) + 1
for case in range(1, num_cases):
  
  r0 = f.readline().split()
  if (r0 == []):
    r0 = f.readline().split()
  r1 = f.readline().split()
  r2 = f.readline().split()
  r3 = f.readline().split()
  board = [r0, r1, r2, r3]
#  print r0
#  print r1
#  print r2
#  print r3
#  print board
  print_tic_tac(case, board, o)

