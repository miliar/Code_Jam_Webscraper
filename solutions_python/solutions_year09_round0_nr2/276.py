f = open('./B-large.in', 'r')
t = int(f.readline())
for x in range(t):
  hw = f.readline().split(' ')
  h = int(hw[0])
  w = int(hw[1])
  #print str(h) + ', ' + str(w)
  cell = []
  for i in range(h):
    row = f.readline().split(' ')
    for j in range(w):
      cell.append([int(row[j])])

  def get_n(num):
    if num - w >= 0:
      return num - w
    else:
      return num

  def get_w(num):
    if num % w > 0:
      return num - 1
    else:
      return num

  def get_e(num):
    if num % w < w - 1:
      return num + 1
    else:
      return num

  def get_s(num):
    if num + w < h * w:
      return num + w
    else:
      return num

  for i in range(h):
    for j in range(w):
      num = i * w + j
      cell[num].append(cell[get_n(num)][0])
      cell[num].append(cell[get_w(num)][0])
      cell[num].append(cell[get_e(num)][0])
      cell[num].append(cell[get_s(num)][0])

      # check sink
      if cell[num][0] <= cell[num][1] and \
         cell[num][0] <= cell[num][2] and \
         cell[num][0] <= cell[num][3] and \
         cell[num][0] <= cell[num][4]:
        cell[num].append('sink')
      # check north
      elif cell[num][1] <= cell[num][2] and \
           cell[num][1] <= cell[num][3] and \
           cell[num][1] <= cell[num][4]:
        cell[num].append('north')
      # check west
      elif cell[num][2] <= cell[num][1] and \
           cell[num][2] <= cell[num][3] and \
           cell[num][2] <= cell[num][4]:
        cell[num].append('west')
      # check east
      elif cell[num][3] <= cell[num][1] and \
           cell[num][3] <= cell[num][2] and \
           cell[num][3] <= cell[num][4]:
        cell[num].append('east')
      # check south
      elif cell[num][4] <= cell[num][1] and \
           cell[num][4] <= cell[num][2] and \
           cell[num][4] <= cell[num][3]:
        cell[num].append('south')

  for i in range(h):
    for j in range(w):
      num = i * w + j
      cell[num].append(-1)

  def go_river(num):
    if num != get_n(num) and cell[get_n(num)][6] == -1:
      if cell[num][5] == 'north' or cell[get_n(num)][5] == 'south':
        cell[get_n(num)][6] = cell[num][6]
        go_river(get_n(num))
    if num != get_w(num) and cell[get_w(num)][6] == -1:
      if cell[num][5] == 'west' or cell[get_w(num)][5] == 'east':
        cell[get_w(num)][6] = cell[num][6]
        go_river(get_w(num))
    if num != get_e(num) and cell[get_e(num)][6] == -1:
      if cell[num][5] == 'east' or cell[get_e(num)][5] == 'west':
        cell[get_e(num)][6] = cell[num][6]
        go_river(get_e(num))
    if num != get_s(num) and cell[get_s(num)][6] == -1:
      if cell[num][5] == 'south' or cell[get_s(num)][5] == 'north':
        cell[get_s(num)][6] = cell[num][6]
        go_river(get_s(num))

  type = 0
  for i in range(h):
    for j in range(w):
      num = i * w + j
      if cell[num][6] == -1:
        cell[num][6] = type
        type += 1
        go_river(num)

  print 'Case #' + str(x + 1) + ':'
  for i in range(h):
    line = ''
    for j in range(w):
      num = i * w + j
      line += chr(ord('a') + cell[num][6])
      if j % w < w - 1:
        line += ' '
    print line

