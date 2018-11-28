f = open('A-large.in')
o = open('output.txt', 'w')
n = int(f.readline())

def check(arr, x, y):
  poss = []
  for i in range(x):
    if arr[i][y] != '.':
      poss.append('^')
      break
  for i in range(x+1,len(arr)):
    if arr[i][y] != '.':
      poss.append('v')
      break
  for j in range(y):
    if arr[x][j] != '.':
      poss.append('<')
      break
  for j in range(y+1, len(arr[0])):
    if arr[x][j] != '.':
      poss.append('>')
      break
  return poss

for i in range(n):
  r,c = [int(x) for x in f.readline().strip().split(" ")]
  grid = []
  for j in range(r):
    row = f.readline().strip()
    grid.append(row)
  count = 0
  #print grid
  for j in range(r):
    for k in range(c):
      if grid[j][k] != '.':
        #print j,k,check(grid,j,k)
        res = check(grid,j,k)
        if res == []:
          count = -1
          break
        if grid[j][k] not in res:
          count += 1
    if count == -1:
      break
  if count == -1:
    o.write('Case #'+str(i+1)+': IMPOSSIBLE\n')
  else:
    o.write('Case #'+str(i+1)+': '+str(count)+'\n')
f.close()
o.close()