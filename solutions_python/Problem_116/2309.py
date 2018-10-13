# Winning sequence is row 1-4, col 1-4, the leading diagonal, or the other diagonal
# only.
def generateWinningTracker():
   return {
   'row': set(range(4)),
   'col': set(range(4)),
   'diagonal': set()
   }

def _diagonal0(grid, player):
   assert player in ('X', 'O')
   for i in range(len(grid)):
      if grid[i][i] not in (player, 'T'):
         return False

   return True

def _diagonal1(grid, player):
   assert player in ('X', 'O')
   for i in range(len(grid)):
      if grid[i][len(grid)-1-i] not in (player, 'T'):
         return False
   return True

def diagonal(grid, player):
   return _diagonal0(grid, player) or _diagonal1(grid, player)

def findWinner(grid):
   if diagonal(grid, 'X'):
      return 'X won'

   if diagonal(grid, 'O'):
      return 'O won'

   OWins = generateWinningTracker()
   XWins = generateWinningTracker()

   # To make the code simple, but efficient, we extract the individual locations
   # of 'X's and 'O's
   locationOfOs = set()
   locationOfXs = set()

   gridHasEmptyCell = False
   for (row_index, row) in enumerate(grid):
      for (col_index, col) in enumerate(row):
         if row[col_index] == 'O':
            locationOfOs.add((row_index, col_index))
         elif row[col_index] == 'X':
            locationOfXs.add((row_index, col_index))
         elif row[col_index] == '.':
            gridHasEmptyCell = True
            locationOfOs.add((row_index, col_index))
            locationOfXs.add((row_index, col_index))


   # Remove all the rows/cols from X that contain an 'O'
   XWins['row'] -= set(i for (i, _) in locationOfOs)
   XWins['col'] -= set(i for (_, i) in locationOfOs)
   # Vice-versa
   OWins['row'] -= set(i for (i, _) in locationOfXs)
   OWins['col'] -= set(i for (_, i) in locationOfXs)

   # Check only the possible wins of each for a winner
   # for row_i in OWins['row']:
   if OWins['row'] or OWins['col']:
      return 'O won'
   elif XWins['row'] or XWins['col']:
      return 'X won'
   elif gridHasEmptyCell:
      return 'Game has not completed'
   else:
      return 'Draw'

def test():
   print 'Running tests...'

   assert findWinner([
   ['X','X','X','T'],
   ['.','.','.','.'],
   ['O','O','.','.'],
   ['.','.','.','.']
   ]) == 'X won'

   assert findWinner([
   ['X','O','X','T'],
   ['X','X','O','O'],
   ['O','X','O','X'],
   ['X','X','O','O']
   ]) == 'Draw'

   assert findWinner([
   ['X','O','X','.'],
   ['O','X','.','.'],
   ['.','.','.','.'],
   ['.','.','.','.']
   ]) == 'Game has not completed'

   assert findWinner([
   ['O','O','X','X'],
   ['O','X','X','X'],
   ['O','X','.','T'],
   ['O','.','.','O']
   ]) == 'O won'

   assert findWinner([
   ['X','X','X','O'],
   ['.','.','O','.'],
   ['.','O','.','.'],
   ['T','.','.','.']
   ]) == 'O won'

   assert findWinner([
   ['O','X','X','X'],
   ['X','O','.','.'],
   ['.','.','O','.'],
   ['.','.','.','O']
   ]) == 'O won'

   print 'Done!'

number_of_test_cases = int(raw_input())
for test_case_i in range(1, number_of_test_cases + 1):
   grid = []
   for row in range(4):
      grid.append(list(raw_input()))

   print 'Case #%s: %s' % (test_case_i, findWinner(grid))

   # Absorb empty line
   if test_case_i < number_of_test_cases:
      raw_input()
