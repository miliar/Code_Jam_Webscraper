import math
import re
import sys

def main():

  lines = [x.strip() for x in sys.stdin.readlines()]

  num_cases = int(lines[0])
  line_num = 1
  #print num_cases
  
  for i in range (0,num_cases):
    found_winner = False
    winner = None
    grid = lines[(i*5)+1:((i*5)+1)+4]
    #print grid
    
    # Check the rows first
    for row in grid:
      first_val = None
      broken = False
      for col in row:
        if first_val is None:
          if col is not "T":
            first_val = col
            if first_val is not "X" and first_val is not "O":
              broken = True
              break
        elif col is not first_val and col is not "T":
          broken = True
          break
      if broken is False:
        found_winner = True
        winner = first_val
        #print "row", row, col, winner
      
    # Check the cols next  
    if found_winner is False:
      for col in range (0, 4):
        first_val = None
        broken = False      
        for row in grid:
          if first_val is None:
            if row[col] is not "T":
              first_val = row[col]
              if first_val is not "X" and first_val is not "O":
                broken = True
                break
          elif row[col] is not first_val and row[col] is not "T":
            broken = True
            break
        if broken is False:
          found_winner = True
          winner = first_val      
          #print "column", row, col, winner              

    # Check the diagonals last  
    if found_winner is False:
      first_val = None
      broken = False 
      for cell in range(0,4):     
        if first_val is None:
          if grid[cell][cell] is not "T":
            first_val = grid[cell][cell]
            if first_val is not "X" and first_val is not "O":
              broken = True
              break
        elif grid[cell][cell] is not first_val and grid[cell][cell] is not "T":
          broken = True
          break           
      if broken is False:
        found_winner = True
        winner = first_val
        #print "diagonal", cell, winner

    if found_winner is False:
      first_val = None
      broken = False   
      for cell in range(0,4):   
        if first_val is None:
          if grid[cell][3-cell] is not "T":
            first_val = grid[cell][3-cell]
            if first_val is not "X" and first_val is not "O":
              broken = True
              break
        elif grid[cell][3-cell] is not first_val and grid[cell][3-cell] is not "T":
          broken = True
          break
      if broken is False:
        found_winner = True
        winner = first_val
        #print "back diagonal", cell, winner
    
    if found_winner is False:
      #check for a draw
      not_completed = False
      for row in grid:
        for col in row:
          if col is ".":
            not_completed = True
    
    if found_winner is True:
      print "Case #" + str(i+1) + ": " + winner + " won"
    elif not_completed is True:
      print "Case #" + str(i+1) + ": Game has not completed"
    else:
      print "Case #" + str(i+1) + ": Draw"
if __name__ == "__main__":
  main()