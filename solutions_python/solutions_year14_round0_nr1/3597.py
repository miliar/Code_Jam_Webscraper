import sys

def read_grid():
  grid = []
  for x in range(4):
    grid.append(map(int, sys.stdin.readline().strip().split(' ')))

  return grid


for case in range(int(sys.stdin.readline())):
  # make grid:
  answer1 = int(sys.stdin.readline())
  grid1 = read_grid()

  answer2 = int(sys.stdin.readline())
  grid2 = read_grid()

  num = 0
  common = 0
  for j in grid2[answer2-1]:
    if j in grid1[answer1-1]:
      common = common + 1
      num = j


  print "Case #" + str(case+1) + ":",
  if (common > 1):
    print "Bad magician!"
  elif common == 0:
    print "Volunteer cheated!"
  else:
    print num

