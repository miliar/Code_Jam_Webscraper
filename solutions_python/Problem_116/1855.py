def checkWinner(B, s):
  for col in xrange(4):
    cnt = 0  
    for i in xrange(4):
      if B[col][i] == s or B[col][i] == 'T':
        cnt += 1
    if cnt == 4:
      return True
  for row in xrange(4):
    cnt = 0  
    for i in xrange(4):               
      if B[i][row] == s or B[i][row] == 'T':
        cnt += 1
    if cnt == 4:
      return True
  cnt = 0  
  for i in xrange(4):
    if B[i][3-i] == s or B[i][3-i] == 'T':
      cnt += 1
  if cnt == 4:
    return True
  cnt = 0
  for i in xrange(4):
    if B[i][i] == s or B[i][i] == 'T':
      cnt += 1
  if cnt == 4:
    return True
  return False

def isFinished(B):
  for i in xrange(4):
    for j in xrange(4):
      if B[i][j] == '.':
        return False
  return True

fin = open("in.txt", "r")
T = int(fin.readline())
B = [None for i in xrange(4)]
for i in xrange(T):
  for j in xrange(4):
    B[j] = list(fin.readline())
  k = i+1
  if checkWinner(B, 'X'):
    print "Case #%d: X won" % k
  elif checkWinner(B, 'O'):
    print "Case #%d: O won" % k
  elif isFinished(B):
    print "Case #%d: Draw" % k
  else:
    print "Case #%d: Game has not completed" % k
  fin.readline()
    
