import sys

sys.setrecursionlimit(10000) # Fucking Python

def cookie_clicker(C, F, X, CPS = 2, TOTAL = 0):
  buy = C/CPS
  wait = X/CPS
  opt1 = TOTAL + wait
  opt2 = TOTAL + buy + X/(CPS + F)
  if opt1 < opt2:
    return wait
  else:
    return buy + cookie_clicker(C, F, X, CPS + F, TOTAL + buy)

lines =[]
for line in open(sys.argv[1]):
  line = line.strip()
  line = line.split(" ")
  line = map(float, line)
  lines.append(line)

for i in range(1, int(lines[0][0]) + 1):
  print("Case #%d: %.7f" % (i, cookie_clicker(lines[i][0], lines[i][1], lines[i][2])))
