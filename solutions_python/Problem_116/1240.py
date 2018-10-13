import sys

def checkwin(p,m):
  for row in m:
    count = 0
    for item in row:
      if (item == p or item == 'T'):
        count = count+1
      else:
        break
    if (count == 4):
      return True
  return False

def checkdiag(p,m):
  count = 0
  count2 = 0
  for i in range(4):
    if(m[i][i] == p or m[i][i] == 'T'):
      count = count+1
    if(m[i][3-i] == p or m[i][3-i] == 'T'):
      count2 = count2+1
  if(count == 4 or count2 == 4):
    return True
  return False

def pointin(m):
  for row in m:
    if('.' in row):
      return True
  return False

T = int(input())
out = ""
f = open('out.txt', "w")

for t in range(T):
  matrix = [[0 for x in range(4)] for x in range(4)]
  # matrix = ["" for x in range(4)]
  xwin = False
  owin = False
  for i in range(4):
    line = sys.stdin.readline()
    for j in range(4):
      matrix[i][j] = line[j]
  if(checkwin('X',matrix) or checkdiag('X',matrix) or checkwin('X',[[row[i] for row in matrix] for i in range(4)])):
    xwin = True
  if(checkwin('O',matrix) or checkdiag('O',matrix) or checkwin('O',[[row[i] for row in matrix] for i in range(4)])):
    owin = True

  if(xwin and not(owin)):
    out += "Case #"+str(t+1)+": X won\n"
  elif(owin and not(xwin)):
    out += "Case #"+str(t+1)+": O won\n"
  elif(pointin(matrix)):
    out += "Case #"+str(t+1)+": Game has not completed\n"
  else:
    out += "Case #"+str(t+1)+": Draw\n"
  sys.stdin.readline()
f.write(out)