import sys

def checkline(a, x, y, xd, yd):
  res = {}
  res["X"] = 0
  res["O"] = 0
  res["."] = 0
  res["T"] = 0
  for i in [0, 1, 2, 3]:
    #print a[x+i*xd][y+i*yd]
    res[a[x+i*xd][y+i*yd]] = res[a[x+i*xd][y+i*yd]]+1
  #print a, x, y, xd, yd,res
  if res["X"] == 4:
    return "X won"
  if res["X"] == 3 and res["T"] == 1:
    return "X won"
  if res["O"] == 4:
    return "O won"
  if res["O"] == 3 and res["T"] == 1:
    return "O won"
  return ""

def check():
  a = []
  a.append(sys.stdin.readline())
  a.append(sys.stdin.readline())
  a.append(sys.stdin.readline())
  a.append(sys.stdin.readline())
  sys.stdin.readline()
  for x in [0, 1, 2, 3]:
    res = checkline(a, x, 0, 0, 1)
    if res != "":
      return res
  for y in [0, 1, 2, 3]:
    res = checkline(a, 0, y, 1, 0)
    if res != "":
      return res
  res = checkline(a, 0, 0, 1, 1)
  if res != "":
    return res
  res = checkline(a, 0, 3, 1, -1)
  if res != "":
    return res
  for x in [0, 1, 2, 3]:
    for y in [0, 1, 2, 3]:
      if a[x][y] == ".":
        return "Game has not completed"
  return "Draw"

T = int(sys.stdin.readline())
for i in range(T):
  print "Case #%d: %s" % (i+1, check())
