nb_tc = input()

def verify_won2(c, i, j, t, di, dj, n):
  if n == 3:
    return True
  i += di
  j += dj
  if 0 <= i < 4 and 0 <= j < 4 and (t[i][j] == c or t[i][j] == 'T'):
    return verify_won2(c, i, j, t, di, dj, n+1)
  else:
    return False

def verify_won(c, i, j, t):
 return verify_won2(c,i,j,t,1,1,0) or \
 verify_won2(c,i,j,t,1,-1,0) or \
 verify_won2(c,i,j,t,-1,1,0) or \
 verify_won2(c,i,j,t,-1,-1,0) or \
 verify_won2(c,i,j,t,0,1,0) or \
 verify_won2(c,i,j,t,0,-1,0) or \
 verify_won2(c,i,j,t,1,0,0) or \
 verify_won2(c,i,j,t,-1,0,0)

for itc in xrange(nb_tc):
  t = (raw_input(),raw_input(),raw_input(),raw_input())
  raw_input().split(' ')
  
  won = False
  for i in range(4):
    for j in range(4):
      if not won and t[i][j] != "T" and t[i][j] != ".":
        won = verify_won(t[i][j], i, j, t)
        if won:
          print "Case #%d: %s won" % (itc+1,t[i][j])
  if not won:
    completed = True
    for l in t:
      for c in l:
        if c == ".":
          completed = False
    if not completed:
      print "Case #%d: Game has not completed" % (itc+1)
    else:
      print "Case #%d: Draw" % (itc+1)

