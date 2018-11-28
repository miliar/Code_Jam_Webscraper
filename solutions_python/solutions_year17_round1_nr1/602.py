# Carly Smith
# Google Code Jam 2017
def cake():
  with open('A-large.in') as f:
    content = f.readlines()

  content = [x.strip('\n') for x in content]

  T = int(content[0])
  start = 1
  for i in range(1,T+1):
    R, C = content[start].split()
    start += 1
    R = int(R)
    C = int(C)
    grid = []

    split = False

    for j in range(0,R):
      line = content[start+j]
      if '?' in line:
        split = True
      grid.append(list(line))

    #print split
    #print grid
    start += R

    if split:
      grid = split_cake(grid)

    print 'Case #{0}:'.format(i)
    for line in range(0,len(grid)):
      print ''.join([str(x) for x in grid[line]])

def split_cake(grid):
  for line in range(0,len(grid)):
    line_str = ''.join([str(x) for x in grid[line]])
    for c in range(0,len(line_str)):
      if line_str[c] != '?' and c+1 < len(line_str):
        if line_str[c+1] == '?':
          grid[line][c+1] = line_str[c]
          line_str = ''.join([str(x) for x in grid[line]])
          # print grid

  for line in range(len(grid)-1,-1,-1):
    line_str = ''.join([str(x) for x in grid[line]])
    for c in range(len(line_str)-1,-1,-1):
      if line_str[c] != '?' and c-1 > -1:
        if line_str[c-1] == '?':
          grid[line][c-1] = line_str[c]
          line_str = ''.join([str(x) for x in grid[line]])
          # print grid

  line_down = False
  for line in range(0,len(grid)):
    line_str = ''.join([str(x) for x in grid[line]])
    if not '?' in line_str:
      line_down = True
    else:
      if line_down:
        new_line_str = ''.join([str(x) for x in grid[line-1]])
        grid[line] = [x for x in new_line_str]
        # print grid

  line_up = False
  for line in range(len(grid)-1,-1,-1):
    line_str = ''.join([str(x) for x in grid[line]])
    if not '?' in line_str:
      line_up = True
    else:
      if line_up:
        new_line_str = ''.join([str(x) for x in grid[line+1]])
        grid[line] = [x for x in new_line_str]
        # print grid

  # print grid
  return grid

if __name__ == '__main__':
  cake()
