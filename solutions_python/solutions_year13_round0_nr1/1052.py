f = open('A-large.in', 'r')
fo = open('A-large.out', 'w')
def ip():
  global f
  return f.readline()

coordinates = [
  [
    [0,1,2,3],
    [0,1,2,3]
  ],
  [
    [3,2,1,0],
    [0,1,2,3]
  ]
]

for i in xrange(4):
  coordinates.append([range(4),[i,i,i,i]])
  coordinates.append([[i,i,i,i],range(4)])
  
num_cases = int(ip())

def winner(xs, ys, board):
  ret = 'N'
  t_count = 0
  x_count = 0
  o_count = 0
  had_dot = False
  for x, y in zip(xs, ys):
    if board[x][y] == 'T':
      t_count += 1
    if board[x][y] == 'X':
      x_count += 1
    if board[x][y] == 'O':
      o_count += 1
    if board[x][y] == '.':
      return '.'
  if t_count == 1:
    if x_count == 3:
      return 'X'
    if o_count == 3:
      return 'O'
  if x_count == 4:
    return 'X'
  if o_count == 4:
    return 'O'
  return 'N'
    

for case in xrange(num_cases):
  board = [list(ip()),list(ip()),list(ip()),list(ip())]
  ip()
  coord_ind = 0
  found_empty = False
  win = 'N'
  while win == 'N' and coord_ind < len(coordinates):
    w = winner(coordinates[coord_ind][0], coordinates[coord_ind][1], board)
    if w == '.':
      found_empty = True
    elif w != 'N':
      win = w
    coord_ind += 1
  if win == 'N' and found_empty == True:
    out = 'Game has not completed'
  elif win == 'N':
    out = 'Draw'
  else:
    out = win + ' won'
  fo.write("Case #%d: %s\n" % (case+1, out))