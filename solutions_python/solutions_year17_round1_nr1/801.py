def A(R, C, data):
  cake = {}
  marked = {}
  for y in range(0, R):
    cake[y] = {}
    marked[y] = {}
    for x in range(0, C):
      cake[y][x] = data[y][x]
      marked[y][x] = False

  total = R*C

  for y in range(0,R):
    for x in range(0,C):
      if not marked[y][x]:
        tup = maxCake(cake,y,x,1,1)
        l = letter(cake,y,x,tup[0],tup[1])
        total -= tup[0]*tup[1]
        for i in range(y,y+tup[0]):
          for j in range(x, x+tup[1]):
            marked[i][j] = True
            cake[i][j] = l
        #print (l,y,x, tup)
        #print printCake(cake)
        #print printMarked(marked)
        if total == 0:
          return printCake(cake)

  return "BLAM"

def printCake(cake):
  result = "\n"
  for i in range(0,len(cake)):
    for j in range(0,len(cake[i])):
      result += cake[i][j]
    result += "\n"
  return result

def printMarked(marked):
  result = "\n"
  for i in range(0,len(marked)):
    for j in range(0,len(marked[i])):
      if marked[i][j]:
        result += "1"
      else:
        result += "0"
    result += "\n"
  return result

def maxCake(cake, y, x, h, w):
  if validCake(cake,y,x,h+1,w):
    t = maxCake(cake,y,x,h+1,w)
    l = letter(cake,y,x,t[0],t[1])
    if l != '?':
      return t
  if validCake(cake,y,x,h,w+1):
    t = maxCake(cake,y,x,h,w+1)
    l = letter(cake,y,x,t[0],t[1])
    if l != '?':
      return t
  return (h,w)

def validCake(cake,y,x,h,w):
  letters = {}
  for i in range(y,y+h):
    for j in range(x,x+w):
      if i not in cake:
        return False
      if j not in cake[i]:
        return False
      l = cake[i][j]
      if l != '?':
        letters[l] = 1
      if len(letters) > 1:
        return False
  return True

def letter(cake,y,x,h,w):
  for i in range(y,y+h):
    for j in range(x,x+w):
      if cake[i][j] != '?':
        return cake[i][j]
  return '?'

def Parse():
  fin = open(r"/Users/tylerbicshel/codejam_2017/A/A-small-attempt1.in", 'r')
  fout = open(r"/Users/tylerbicshel/codejam_2017/A/A-small-attempt1.out", 'w')
  count = int(fin.readline())
  for i in range(1, count+1):
    line = fin.readline().rstrip().split(" ")
    R = int(line[0])
    C = int(line[1])

    cake = []
    for j in range(0, R):
      line = fin.readline().rstrip()
      cake.append(line)

    ret = A(R, C, cake)
    result = "Case #%d: %s" % (i, ret)
    print result
    fout.write(result)
  fin.close()
  fout.close()

Parse()
