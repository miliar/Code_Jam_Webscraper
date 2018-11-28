#!usr/bin/python 
import math 
import time 

t0 = time.clock()
out = open('myfile','w')
def check(row):
  if len(row) != 4:
    print "uh oh......................." , len(row)
  if 'T' in row:
      if row.count('X') == 3:
        print 'x won' + row 
        return 1 #'X won'
      elif row.count('O') == 3:
         print 'o won' + row 
         return -1 #'O won'
  if row.count('X') == 4 :
     print 'x won' + row 
     return 1 #'X won'
  if row.count('O') == 4 :
    print '0 won' + row 
    return -1 #'O won'
  return  0 #"Game has not completed" 
def play (game):
    cnum = -1;
    while (cnum < 3):
      cnum = cnum+1
      ans = check(game[cnum::4])
      if ans != 0:
          return ans
    ans = check(game[0::5])
    if ans != 0:
      return ans
    ans = check(game[:13][3::3]) 
    if ans != 0: 
      return ans
    if game.count('.') == 0:
      return 99
    return 0

with   open('input.txt') as f:

  cases =  int( f.readline().rstrip())
  
  h = {0:"Game has not completed" , 1 : 'X won', -1: 'O won', 99: 'Draw'}
  for c in range(1,cases+1):
    print c
    game = ''
    res = 0
    
    for r in range(0,4):
      row = f.readline()[0:4]
      
      if res == 0 : #nobody has won yet
         res = check(row)
         game = game + row
    print game
    f.readline()
    
    if res == 0:
        print "rows done"
        res =  play(game)
    #
    
    out.write(  "Case #" + str(c) + ": " + h[res] + "\n")
    
out.close()
f.close()
print ( time.clock() - t0)