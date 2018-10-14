ADJ_CELLS = [(-1,-1), (-1,0), (0,1), (1,0), (1,-1), (1,1), (-1,1), (0,-1)]
ADJ_CELLS_FULL = [(-1,-1), (-1,0), (0,1), (1,0), (1,-1), (1,1), (-1,1), (0,-1)]

def yieldSubset(seq, r):
    if r:
        for i in xrange(r - 1, len(seq)):
            for cl in yieldSubset(seq[:i], r - 1):
                yield cl + (seq[i],)
    else:
      yield tuple()

      
def checkOneGame(x1,y1, mines, it):
  def generateGrid(mines):
    l = None
    grid = [[-1]*(y1) for w in range(x1)]
    for i in mines:
      grid[i[0]][i[1]] = "*"
    for x in range(x1):
      for y in range(y1):
        if grid[x][y] <> "*":
          settedMines = len([(x+i[0],y+i[1]) for i in ADJ_CELLS
                                if -1<x+i[0]<x1 and -1<y+i[1]<y1
                                and grid[x+i[0]][y+i[1]] == "*"])
          grid[x][y] = settedMines
          if settedMines == 0:
            l = (x,y)
    return grid, l

  def isValid(x,y, grid, r):
    def checkGrid(x, y):
      r[0] +=1
      if grid[x][y] == 0: 
        grid[x][y] = "#" 
        for i in ADJ_CELLS: # BFS on the grid
          if -1<x+i[0]<x1 and -1<y+i[1]<y1:
            if  grid[x+i[0]][y+i[1]] not in ["*", "#"] :
              checkGrid(x+i[0],y+i[1])
      else: grid[x][y] = "#"

    checkGrid(x,y)
    return x1*y1 - mines - r[0] == 0

  seter = [(i,j) for i in range(x1) for j in range(y1)]
  for i in yieldSubset(seter, mines):
    g, l = generateGrid(i)
    if l <> None:
      if  isValid(l[0], l[1], g, [0]):  
        print("Case #"+str(it+1)+": ")
        for i in range(x1):   
          for j in range(y1):
            if g[i][j] <> "*": g[i][j] = "."
        g[l[0]][l[1]] = "c"
        for i in g:
          print "".join(i)
        return True
    elif x1*y1 == mines + 1:
      print("Case #"+str(it+1)+": ")
      for i in range(x1):   
          for j in range(y1):
            if g[i][j] <> "*": g[i][j] = "c"
      for i in g:
          print "".join(i)
      return True

  print("Case #"+str(it+1)+": ")
  print("Impossible")
  return False


if __name__ == '__main__':
    numberOfGames = int(raw_input())
    for i in range(numberOfGames):
      datas = map(int, raw_input().split())
      checkOneGame(datas[0],datas[1] ,datas[2] , i )
