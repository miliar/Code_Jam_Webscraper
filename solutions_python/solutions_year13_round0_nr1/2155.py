a  = open('A-large.in','r')
b = int(a.readline()[0:4])
result = ['' for x in range(b)]
board = [[["" for x in range(4)] for x in range(4)] for x in range(b)] 
for x in range(b):
  for q in range(4):
      c = a.readline()
      for w in range(5):
        if(c[w-1:w] != ''):
          board[x][q][w-1] = c[w-1:w]
  a.readline()
e = ''

p, r, t, y = '', '', '', ''
for z in range(b):
  for a in range(4):
    p = p + str(board[z][a][0])
    r = r + str(board[z][a][1])
    t = t + str(board[z][a][2])
    y = y + str(board[z][a][3])  
  if(p == 'XXXT' or p == 'XXTX' or p == 'XTXX' or p == 'TXXX' or p == 'XXXX' or r == 'XXXT' or r == 'XXTX' or r == 'XTXX' or r == 'TXXX' or r == 'XXXX' or t == 'XXXT' or t == 'XXTX' or t == 'XTXX' or t == 'TXXX' or t == 'XXXX' or y == 'XXXT' or y == 'XXTX' or y == 'XTXX' or y == 'TXXX' or y == 'XXXX'):
    result[z] = 'X won'
  elif(((p[0:1] == 'X') and (r[0:1] == 'X') and (t[0:1] == 'X') and (y[0:1]== 'X')) or ((p[0:1] == 'T') and (r[0:1] == 'X') and (t[0:1] == 'X') and (y[0:1]== 'X')) or ((p[0:1] == 'X') and (r[0:1] == 'T') and (t[0:1] == 'X') and (y[0:1]== 'X')) or ((p[0:1] == 'X') and (r[0:1] == 'X') and (t[0:1] == 'T') and (y[0:1]== 'X')) or ((p[0:1] == 'X') and (r[0:1] == 'X') and (t[0:1] == 'X') and (y[0:1]== 'T'))):
    result[z] = 'X won'
  elif(((p[3:4] == 'X') and (r[2:3] == 'X') and (t[1:2] == 'X') and (y[0:1]== 'X')) or ((p[3:4] == 'T') and (r[2:3] == 'X') and (t[1:2] == 'X') and (y[0:1]== 'X')) or ((p[3:4] == 'X') and (r[2:3] == 'T') and (t[1:2] == 'X') and (y[0:1]== 'X')) or ((p[3:4] == 'X') and (r[2:3] == 'X') and (t[1:2] == 'T') and (y[0:1]== 'X')) or ((p[3:4] == 'X') and (r[2:3] == 'X') and (t[1:2] == 'X') and (y[0:1]== 'T'))):
    result[z] = 'X won'
  elif(((p[0:1] == 'X') and (r[1:2] == 'X') and (t[2:3] == 'X') and (y[3:4]== 'X')) or ((p[0:1] == 'T') and (r[1:2] == 'X') and (t[2:3] == 'X') and (y[3:4]== 'X')) or ((p[0:1] == 'X') and (r[1:2] == 'T') and (t[2:3] == 'X') and (y[3:4]== 'X')) or ((p[0:1] == 'X') and (r[1:2] == 'X') and (t[2:3] == 'T') and (y[3:4]== 'X')) or ((p[0:1] == 'X') and (r[1:2] == 'X') and (t[2:3] == 'X') and (y[3:4]== 'T'))):
    result[z] = 'X won'
  elif(((p[1:2] == 'X') and (r[1:2] == 'X') and (t[1:2] == 'X') and (y[1:2]== 'X')) or ((p[1:2] == 'T') and (r[1:2] == 'X') and (t[1:2] == 'X') and (y[1:2]== 'X')) or ((p[1:2] == 'X') and (r[1:2] == 'T') and (t[1:2] == 'X') and (y[1:2]== 'X')) or ((p[1:2] == 'X') and (r[1:2] == 'X') and (t[1:2] == 'T') and (y[1:2]== 'X')) or ((p[1:2] == 'X') and (r[1:2] == 'X') and (t[1:2] == 'X') and (y[1:2]== 'T'))):
    result[z] = 'X won'
  elif(((p[2:3] == 'X') and (r[2:3] == 'X') and (t[2:3] == 'X') and (y[2:3]== 'X')) or ((p[2:3] == 'T') and (r[2:3] == 'X') and (t[2:3] == 'X') and (y[2:3]== 'X')) or ((p[2:3] == 'X') and (r[2:3] == 'T') and (t[2:3] == 'X') and (y[2:3]== 'X')) or ((p[2:3] == 'X') and (r[2:3] == 'X') and (t[2:3] == 'T') and (y[2:3]== 'X')) or ((p[2:3] == 'X') and (r[2:3] == 'X') and (t[2:3] == 'X') and (y[2:3]== 'T'))):
    result[z] = 'X won'
  elif(((p[3:4] == 'X') and (r[3:4] == 'X') and (t[3:4] == 'X') and (y[3:4]== 'X')) or ((p[3:4] == 'T') and (r[3:4] == 'X') and (t[3:4] == 'X') and (y[3:4]== 'X')) or ((p[3:4] == 'X') and (r[3:4] == 'T') and (t[3:4] == 'X') and (y[3:4]== 'X')) or ((p[3:4] == 'X') and (r[3:4] == 'X') and (t[3:4] == 'T') and (y[3:4]== 'X')) or ((p[3:4] == 'X') and (r[3:4] == 'X') and (t[3:4] == 'X') and (y[3:4]== 'T'))):
    result[z] = 'X won'
  elif(((p[0:1] == 'O') and (r[0:1] == 'O') and (t[0:1] == 'O') and (y[0:1]== 'O')) or ((p[0:1] == 'T') and (r[0:1] == 'O') and (t[0:1] == 'O') and (y[0:1]== 'O')) or ((p[0:1] == 'O') and (r[0:1] == 'T') and (t[0:1] == 'O') and (y[0:1]== 'O')) or ((p[0:1] == 'O') and (r[0:1] == 'O') and (t[0:1] == 'T') and (y[0:1]== 'O')) or ((p[0:1] == 'O') and (r[0:1] == 'O') and (t[0:1] == 'O') and (y[0:1]== 'T'))):
    result[z] = 'O won'
  elif(p == 'OOOT' or p == 'OOTO' or p == 'OTOO' or p == 'TOOO' or p == 'OOOO' or r == 'OOOT' or r == 'OOTO' or r == 'OTOO' or r == 'TOOO' or r == 'OOOO' or t == 'OOOT' or t == 'OOTO' or t == 'OTOO' or t == 'TOOO' or t == 'OOOO' or y == 'OOOT' or y == 'OOTO' or y == 'OTOO' or y == 'TOOO' or y == 'OOOO'):
    result[z] = 'O won'
  elif(((p[1:2] == 'O') and (r[1:2] == 'O') and (t[1:2] == 'O') and (y[1:2]== 'O')) or ((p[1:2] == 'T') and (r[1:2] == 'O') and (t[1:2] == 'O') and (y[1:2]== 'O')) or ((p[1:2] == 'O') and (r[1:2] == 'T') and (t[1:2] == 'O') and (y[1:2]== 'O')) or ((p[1:2] == 'O') and (r[1:2] == 'O') and (t[1:2] == 'T') and (y[1:2]== 'O')) or ((p[1:2] == 'O') and (r[1:2] == 'O') and (t[1:2] == 'O') and (y[1:2]== 'T'))):
    result[z] = 'O won'
  elif(((p[2:3] == 'O') and (r[2:3] == 'O') and (t[2:3] == 'O') and (y[2:3]== 'O')) or ((p[2:3] == 'T') and (r[2:3] == 'O') and (t[2:3] == 'O') and (y[2:3]== 'O')) or ((p[2:3] == 'O') and (r[2:3] == 'T') and (t[2:3] == 'O') and (y[2:3]== 'O')) or ((p[2:3] == 'O') and (r[2:3] == 'O') and (t[2:3] == 'T') and (y[2:3]== 'O')) or ((p[2:3] == 'O') and (r[2:3] == 'O') and (t[2:3] == 'O') and (y[2:3]== 'T'))):
    result[z] = 'O won'
  elif(((p[3:4] == 'O') and (r[3:4] == 'O') and (t[3:4] == 'O') and (y[3:4]== 'O')) or ((p[3:4] == 'T') and (r[3:4] == 'O') and (t[3:4] == 'O') and (y[3:4]== 'O')) or ((p[3:4] == 'O') and (r[3:4] == 'T') and (t[3:4] == 'O') and (y[3:4]== 'O')) or ((p[3:4] == 'O') and (r[3:4] == 'O') and (t[3:4] == 'T') and (y[3:4]== 'O')) or ((p[3:4] == 'O') and (r[3:4] == 'O') and (t[3:4] == 'O') and (y[3:4]== 'T'))):
    result[z] = 'O won'
  elif(((p[3:4] == 'O') and (r[2:3] == 'O') and (t[1:2] == 'O') and (y[0:1]== 'O')) or ((p[3:4] == 'T') and (r[2:3] == 'O') and (t[1:2] == 'O') and (y[0:1]== 'O')) or ((p[3:4] == 'O') and (r[2:3] == 'T') and (t[1:2] == 'O') and (y[0:1]== 'O')) or ((p[3:4] == 'O') and (r[2:3] == 'O') and (t[1:2] == 'T') and (y[0:1]== 'O')) or ((p[3:4] == 'O') and (r[2:3] == 'O') and (t[1:2] == 'O') and (y[0:1]== 'T'))):
    result[z] = 'O won'
  elif(((p[0:1] == 'O') and (r[1:2] == 'O') and (t[2:3] == 'O') and (y[3:4]== 'O')) or ((p[0:1] == 'T') and (r[1:2] == 'O') and (t[2:3] == 'O') and (y[3:4]== 'O')) or ((p[0:1] == 'O') and (r[1:2] == 'T') and (t[2:3] == 'O') and (y[3:4]== 'O')) or ((p[0:1] == 'O') and (r[1:2] == 'O') and (t[2:3] == 'T') and (y[3:4]== 'O')) or ((p[0:1] == 'O') and (r[1:2] == 'O') and (t[2:3] == 'O') and (y[3:4]== 'T'))):
    result[z] = 'O won'
  elif(not('.'in p ) and not('.'in r ) and not('.'in t ) and not('.'in y )):
    result[z] =  'Draw'
  else:
    result[z] = 'Game has not completed'
  p, r, t, y = '', '', '', ''
e = ''
n = open('results.out' , 'w')
for x in range(b):
  w = 'Case #{0}: {1}\n'.format(x+1, result[x])
  n.write(w)