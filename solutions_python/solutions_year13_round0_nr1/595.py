def decide(t):
    filled = True
    # hori
    for x in range(4):
      countX = 0
      countO = 0
      countT = 0
      for y in range(4):
        if t[x][y] == 'X':
          countX += 1
        elif t[x][y] == 'O':
            countO += 1
        elif t[x][y] == 'T':
          countT += 1
      if countX + countO + countT < 4:
        filled = False
      if countX + countT >= 4:
        return "X won"
      elif countO + countT >= 4:
        return "O won"
    # verti
    for y in range(4): 
      countX = 0
      countO = 0
      countT = 0
      for x in range(4):
        if t[x][y] == 'X':
          countX += 1
        elif t[x][y] == 'O':
          countO += 1
        elif t[x][y] == 'T':
          countT += 1
      if countX + countT >= 4:
        return "X won"
      elif countO + countT >= 4:
        return "O won"
    # diagonal 
    countX = 0
    countO = 0
    countT = 0
    for x in range(4): 
      if t[x][x] == 'X':
        countX += 1
      elif t[x][x] == 'O':
        countO += 1
      elif t[x][x] == 'T':
        countT += 1
    if countX + countT >= 4:
      return "X won"
    elif countO + countT >= 4:
      return "O won"
    # anti diagonal 
    countX = 0
    countO = 0
    countT = 0
    for x in range(4): 
      if t[x][3-x] == 'X':
        countX += 1
      elif t[x][3-x] == 'O':
        countO += 1
      elif t[x][3-x] == 'T':
        countT += 1
    if countX + countT >= 4:
      return "X won"
    elif countO + countT >= 4:
      return "O won"
    if filled:
      return "Draw"
    else:
      return "Game has not completed"
       
def solve():
#  f = open("in.txt", 'r')
#  f = open("A-small-attempt0.in", 'r')
  f = open("A-large.in", 'r')
  T = int(f.readline())
  for i in range(T):
    t = [[]] * 4
    for j in range(4):
      l = f.readline()
      t[j] = list(l)
    l = f.readline()
    print "Case #%i:" % (i+1), decide(t)

solve()
