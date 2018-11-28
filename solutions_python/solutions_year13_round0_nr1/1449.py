data = open('a.txt', 'r').read().split('\n')

(T,) = map(int, data.pop(0).split(' '))

row = ['', '', '', '']

def wins(row, symbol):
   goodSymbols = [symbol, 'T']
   for j in range(4):
      if row[j].replace('T', symbol) == symbol*4:
         return True
   
   for j in range(4):
      w = True
      for i in range(4):
         if row[i][j] not in goodSymbols:
            w = False
      if w:
         return True
   
   w = True
   for j in range(4):
      if row[j][j] not in goodSymbols:
         w = False
   
   if w:
      return True
   
   w = True
   for j in range(4):
      if row[3-j][j] not in goodSymbols:
         w = False
   
   return w

def emptySquares(row):
   for j in range(4):
      for i in range(4):
         if row[j][i] == '.':
            return True

   return False

for t in range(T):
   for j in range(4):
      row[j] = data.pop(0)
   
   if wins(row, 'X'):
   	print 'Case #' + str(t+1) + ': X won'
   elif wins(row, 'O'):
      print 'Case #' + str(t+1) + ': O won'
   elif emptySquares(row):
      print 'Case #' + str(t+1) + ': Game has not completed'
   else:
      print 'Case #' + str(t+1) + ': Draw'

   if len(data) != 0:
      data.pop(0)