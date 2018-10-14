#!/usr/bin/env python2

def solveCol(grid, col):

   for j in range(4):
      player = grid[col][j]
      if player not in ('X', 'O'):
         break
      #print player

      for i in range(4):
         if grid[i][j] not in ('T', player):
            break
         #print '   ' + grid[i][j]
         if (i == 3):
            return player

def solveRow(grid, row):

   for i in range(4):
      player = grid[i][row]
      if player not in ('X', 'O'):
         break
      #print player

      for j in range(4):
         if grid[i][j] not in ('T', player):
            break
         #print '   ' + grid[i][j]
         if (j == 3):
            return player

def solveUpDiag(grid, index):

   player = grid[3-index][index]
   if player not in ('X', 'O'):
      return
   #print player

   for n in range(4):
      if grid[3-n][n] not in ('T', player):
         break
      #print '   ' + grid[i][j]
      if (n == 3):
         return player

def solveDownDiag(grid, index):

   player = grid[index][index]
   if player not in ('X', 'O'):
      return
   #print player

   for n in range(4):
      if grid[n][n] not in ('T', player):
         break
      #print '   ' + grid[i][j]
      if (n == 3):
         return player


def solveGrid(grid):
   #print grid

   for n in range(4):

      res = solveCol(grid, n) 
      if res != None:
         return res + " won"

      res = solveRow(grid, n) 
      if res != None:
         return res + " won"

      res = solveUpDiag(grid, n)
      if res != None:
         return res + " won"

      res = solveDownDiag(grid, n)
      if res != None:
         return res + " won"

   for i in range(3):
      for j in range(3):
         if grid[i][j] == '.':
            return "Game has not completed"

   return 'Draw'

def main():

   grids = []

   with open('A-small.in') as fileIn:
      gameNb = int(fileIn.readline())
      lines = fileIn.readlines();
      for game in range(gameNb):
         grid = [[lines[(game*5)+y][r] for r in range(4)] for y in range(4)]
         grids.append(grid)

   out = ''
   for pos, grid in enumerate(grids):
      out += "Case #{i}: {s}\n".format(i=pos+1, s=solveGrid(grid))

   with open('A-small.out', 'w') as fileOut:
      fileOut.write(out)
      print out

if __name__ == "__main__":
   main()
