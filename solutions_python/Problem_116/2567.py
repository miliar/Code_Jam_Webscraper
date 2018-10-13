from numpy import *

def xwin(puz, r, c):
  return puz[r][c] == 'X' or puz[r][c] == 'T'
def owin(puz, r, c):
  return puz[r][c] == 'O' or puz[r][c] == 'T'

def solve(puz):
  x = False
  o = False
  for i in range(4):
    x = x or (xwin(puz,i, 0) and xwin(puz,i,1) and xwin(puz,i,2) and xwin(puz,i,3))
    x = x or (xwin(puz,0,i) and xwin(puz,1,i) and xwin(puz,2,i) and xwin(puz,3,i))

  x = x or (xwin(puz,0,0) and xwin(puz,1,1) and xwin(puz,2,2) and xwin(puz,3,3))
  x = x or (xwin(puz,3,0) and xwin(puz,2,1) and xwin(puz,1,2) and xwin(puz,0,3))

  for i in range(4):
    o = o or (owin(puz,i, 0) and owin(puz,i,1) and owin(puz,i,2) and owin(puz,i,3))
    o = o or (owin(puz,0,i) and owin(puz,1,i) and owin(puz,2,i) and owin(puz,3,i))

  o = o or (owin(puz,0,0) and owin(puz,1,1) and owin(puz,2,2) and owin(puz,3,3))
  o = o or (owin(puz,3,0) and owin(puz,2,1) and owin(puz,1,2) and owin(puz,0,3))

  if x:
    return "X won"
  if o:
    return "O won"
  if ('.' in puz[0]) or ('.' in puz[1]) or ('.' in puz[2]) or ('.' in puz[3]):
    return "Game has not completed"
  return "Draw"

f = open('A-large.in')
ans = open('answer', 'w')
numpuz = int(f.readline())
for l in range(numpuz):
  puz = [['','','',''],['','','',''],['','','',''],['','','','']]
  for j in range(4):
    s = f.readline().strip()
    for k in range(4):
      puz[j][k] = s[k]
  f.readline()
  result = solve(puz)
  ans.write("Case #" + str(l+1) + ": " + result + "\n")
