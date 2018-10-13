T = int(raw_input())

def posibilities(row, grid):
  posibilities = grid[row-1]
  return set( posibilities.split(' ') )


grid1 = ["", "", "", ""]
grid2 = ["", "", "", ""]

for caseNum in range(1, 1 +T):
  row1 = int(raw_input())

  for i in range(4):
    grid1[i] = raw_input();

  row2 = int(raw_input())

  for i in range(4):
    grid2[i] = raw_input();

  pos1 = posibilities(row1, grid1)
  pos2 = posibilities(row2, grid2)
  #print pos1, pos2

  sln = pos1 & pos2




  if len(sln) == 1:
    print "Case #{0}: {1}".format(caseNum, sln.pop())
  elif len(sln) > 1:
    print "Case #{0}: Bad magician!".format(caseNum)
  elif len(sln) == 0:
    print "Case #{0}: Volunteer cheated!".format(caseNum)


  #print sln

