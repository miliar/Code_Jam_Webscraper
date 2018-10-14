import fileinput

fi = fileinput.input()
T = int(fi.readline())

def countC(list):
   count={'O':0, 'X':0, 'T':0, '.':0}
   for c in list:
     count[c]+=1
   return count

def tellWinner(cnt):
   if cnt['O'] + cnt['T'] == 4: return 'O won'
   if cnt['X'] + cnt['T'] == 4: return 'X won'
   return None

def checkWinner(field):
   for row in xrange(4):
      cnt = countC(field[row])
      if tellWinner(cnt):
         return tellWinner(cnt)
   for col in xrange(4):
      cnt = countC([field[row][col] for row in xrange(4)])
      if tellWinner(cnt):
         return tellWinner(cnt)
   cnt = countC([field[row][row] for row in xrange(4)])
   if tellWinner(cnt):
      return tellWinner(cnt)
   cnt = countC([field[3-row][row] for row in xrange(4)])
   if tellWinner(cnt):
      return tellWinner(cnt)
   return None

def checkNotComplete(field):
   for line in field:
      if '.' in line: return 'Game has not completed'
   return None

for caseN in xrange(T):
   field = []
   for rowI in xrange(4):
       row = fi.readline().strip()
       field.append(row)
   #print field
   
   winner = checkWinner(field)
   notComplete = checkNotComplete(field)
   if winner != None:
       print 'Case #'+str(caseN+1)+': '+winner
   elif notComplete != None:
       print 'Case #'+str(caseN+1)+': '+notComplete
   else: print 'Case #'+str(caseN+1)+': Draw'
   fi.readline()

