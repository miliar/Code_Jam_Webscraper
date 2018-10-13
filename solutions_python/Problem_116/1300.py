n = int(raw_input())

ns = 4

def check(d,v,l):
  r = True
  for i in xrange(ns):
    if not d[l[i][0]][l[i][1]] in v:
      return False
  return True
def solve():
  d = []
  for i in xrange(ns):
    d.append(raw_input())
  try:
    raw_input()
  except:
    pass
  xwon = False
  owon = False
  
  for i in xrange(ns):
    cl1 = [ (i,j) for j in xrange(ns) ]
    cl2 = [ (j,i) for j in xrange(ns) ]
    xwon |= check(d, ['X','T'], cl1)
    xwon |= check(d, ['X','T'], cl2)
    owon |= check(d, ['O','T'], cl1)
    owon |= check(d, ['O','T'], cl2)
  xwon |= check(d,['X','T'], [ (0,0),(1,1),(2,2),(3,3)] )
  xwon |= check(d,['X','T'], [ (3,0),(2,1),(1,2),(0,3)] )

  owon |= check(d,['O','T'], [ (0,0),(1,1),(2,2),(3,3)] )
  owon |= check(d,['O','T'], [ (3,0),(2,1),(1,2),(0,3)] )

  if not xwon and not owon and not '.' in ''.join(d):
    return (True, True)
     
  return (xwon, owon)
  
for i in xrange(n):
  rr = solve() 
  print "Case #%d:" % (i+1),
  if rr[0] and not rr[1]:
    print "X won"
  elif rr[0] and rr[1]:
    print "Draw"
  elif not rr[0] and not rr[1]:
    print "Game has not completed"
  elif not rr[0] and rr[1]:
    print "O won"
