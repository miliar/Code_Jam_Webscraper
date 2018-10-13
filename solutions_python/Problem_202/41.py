import math

def getSpiral(n):
    for i in xrange(1, int(math.ceil(n/2.0)) + 1):
        for j in xrange(i, n-i+2):
            yield i,j
            yield j,i
            yield n-i+1,j
            yield j,n-i+1

def getModel(canX, canP):
    if canX and canP:
        return "o"
    elif canX:
        return "x"
    elif canP:
        return "+"

def getKey(x,y):
    return x * 1000 + y

t = int(raw_input())
for i in xrange(1, t + 1): 
  n, m = [int(v) for v in raw_input().split(" ")]  
  
  all = dict()
  row = dict()
  col = dict()
  d1 = dict()
  d2 = dict()
  
  result = 0

  for j in xrange(1, m + 1):
    s, r, c = [v for v in raw_input().split(" ")]
    all[getKey(int(r), int(c))] = s
    if s == "+" or s == "o":
        d1[int(r) - int(c)] = 1
        d2[int(r) + int(c)] = 1
        result += 1
    if s == "x" or s == "o":
        row[int(r)] = 1
        col[int(c)] = 1
        result += 1

  added = []

  for dx,dy in getSpiral(n):
    key = getKey(dx,dy)
    isX = all.__contains__(key) and (all[key] == "x" or all[key] == "o")
    isP = all.__contains__(key) and (all[key] == "+" or all[key] == "o") 
    changed = False   
    if ((not isX) and row.__contains__(dx) == 0 and col.__contains__(dy) == 0):
        row[dx] = 1
        col[dy] = 1
        isX = True
        result += 1
        changed = True
    if ((not isP) and d1.__contains__(dx-dy) == 0 and d2.__contains__(dx+dy) == 0):
        d1[dx-dy] = 1
        d2[dx+dy] = 1
        isP = True
        result += 1
        changed = True
    if (changed):
        all[key] = getModel(isX,isP)
        added.append("{} {} {}".format(getModel(isX, isP), dx, dy))

  print("Case #{}: {} {}".format(i, result, len(added)))
  for mm in added:
    print(mm)