n = int(raw_input())

def count(l,sym=["X","O"],uni="T"):
  for y in sym:
    if(l.count(y)+l.count(uni))==4:
      return True,y
  return False, None

for x in range(n):
  t = []
  dots = 0
  for y in range(4):
    l = t.append(raw_input())
    dots += t[y].count(".")
  win = False
  sym = None
  for y in range(4):
    line = t[y]
    row = [t[i][y] for i in range(4)]
    win,sym=count(line)
    if(win):
      break
    win,sym = count(row)
    if(win):
      break
  if(not win):
    diagLeft = [t[i][i] for i in range(4)]
    win,sym = count(diagLeft)
  if(not win):
    diagRight=[t[i][3-i] for i in range(4)]
    win,sym = count(diagRight)
  if(win):
    print "Case #%s: %s won" % (x+1,sym)
  elif dots==0:
    print "Case #%s: Draw" % (x+1)
  else:
    print "Case #%s: Game has not completed" % (x+1)

  if (x+1!=n):
    raw_input()