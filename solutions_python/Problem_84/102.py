import sys, re

class Pos():
  def __init__(self,P,V,D):
    self.P = P

def comp(A,B):
  return cmp(float(A.P),float(B.P))


where = [[0,0], [0,1], [1,0], [1,1]]
red = ['/','\\','\\','/']
cases = sys.stdin.readline()


for case in range(0,int(cases)):
  H,W = [int(x) for x in sys.stdin.readline().split()]
  grid = []
  for i in range(0,H):
    grid.append( [str(ch) for ch in sys.stdin.readline()] )
  for row in range(0,H):
    for col in range(0,W):
      if grid[row][col]=='#':
        for whi in range(0,4):
          if row+where[whi][0]>=H or col+where[whi][1]>=W or (grid[row+where[whi][0]][col+where[whi][1]]=='.'): 
            grid[row][col]='#'
            break
          grid[row+where[whi][0]][col+where[whi][1]]=red[whi]

  ok = True
  for row in grid:
    if ok==False: break
    for ch in row:
      if ch=='#':
        ok = False
        break

  print "Case #%d:" % (case+1)
  if not ok:
    print "Impossible"
  else:
    for row in grid:
      for i in range(0,W):
        sys.stdout.write(row[i])
      print ""
