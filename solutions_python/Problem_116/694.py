
__author__ = 'sergeyy'
import time


def isWon(m, p):
   if m[0][0]+m[1][1]+m[2][2]+m[3][3] == p or m[0][3]+m[1][2]+m[2][1]+m[3][0] == p:
      return True
   for i in range(4):
      if m[i] == p or m[0][i]+m[1][i]+m[2][i]+m[3][i] == p:
         return True
   return False

def isComplete(m):
   for i in range(4):
      if m[i].find(".") != -1:
         return False

   return True


def check(m):
   o = ['','','','']
   x = ['','','','']

   for i in range(4):
      o[i] = m[i].replace('T', 'O')
      x[i] = m[i].replace('T', 'X')

   if isWon(o, 'OOOO'):
      return "O won"

   if isWon(x, 'XXXX'):
      return "X won"

   if not isComplete(m):
      return "Game has not completed"

   return "Draw"

case = 1
m = [["."]*4]*4
with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for i in range(1, cnt+1):
         for j in range(4):
            line = fin.readline()
            m[j] = line[:-1:]

         oline = ''
         oline = 'Case #' + str(i) +': ' + check(m) +'\n'
         fout.write(oline)
         fin.readline()
print (time.clock())



