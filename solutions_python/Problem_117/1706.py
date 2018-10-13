#!/usr/bin/env python2

class square :

   def __init__(self, i, j, grid):
      self.lig = i
      self.col = j
      self.grid = grid
      self.value = grid[i][j]

   def _isPossibleCol(self):
      print " Check colonne :"
      for i in range(len(self.grid)):
         print self.grid[i][self.col] + " > " + self.value + " ?"
         if self.grid[i][self.col] > self.value:
            return False
      return True

   def _isPossibleLig(self):
      print " Check ligne :"
      for j in range(len(self.grid[0])):
         print self.grid[self.lig][j] + " > " + self.value + " ?"
         if self.grid[self.lig][j] > self.value:
            return False
      return True

   def isPossible(self):
      if not self._isPossibleCol():
         return self._isPossibleLig()
      return True 

def solveGrid(grid):
   openSols = []
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         openSols.append(square(i, j, grid))

   openSols.sort(key=lambda square: square.value, reverse=True)
   #for s in openSols:
   #   print s.value

   res = True
   while openSols and res:
      s = openSols.pop()
      print "check de square : [" + str(s.lig) + "," + str(s.col) + "] value = " + str(s.value)
      if not s.isPossible():
         return "NO"
   return "YES"

def main():

   grids = []

   with open('B-small.in') as fileIn:
      gameNb = int(fileIn.readline())

      for game in range(gameNb):
         
         n, m = fileIn.readline().split()
         
         grid = [fileIn.readline().split() for y in range(int(n))]
         grids.append(grid)
         print grid

   out = ''
   for pos, grid in enumerate(grids):
      print "***"
      out += "Case #{i}: {s}\n".format(i=pos+1, s=solveGrid(grid))

   with open('B-small.out', 'w') as fileOut:
      fileOut.write(out)
      print out

if __name__ == "__main__":
   main()
