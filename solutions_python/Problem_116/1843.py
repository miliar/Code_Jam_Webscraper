in_file = open('A-large.in')
n = int(in_file.readline())
#n = 1
def solves(b, s):
  for j in b:
    count = j.count(s)
    if 'T' in j:
      count += 1
    if count == 4:
      return s
    
  for j in range(4):
    a = [b[0][j], b[1][j], b[2][j], b[3][j]]
    count = a.count(s)
    if 'T' in a:
      count += 1
    if count == 4:
      return s
  a = [b[0][0], b[1][1], b[2][2], b[3][3]]
  count = a.count(s)
  if 'T' in a:
    count += 1
  if count == 4:
    return s
  a = [b[0][3], b[1][2], b[2][1], b[3][0]]
  count = a.count(s)
  if 'T' in a:
    count += 1
  if count == 4:
    return s

      
def solve(b):
  m = max(solves(b, 'X'), solves(b, 'O'))
  if m != None:
    return m+' won'
  for j in b:
    if '.' in j:
      return 'Game has not completed'
  return 'Draw'





for i in range(n):
  b = []
  for j in range(4):
    b.append(in_file.readline().strip())
  in_file.readline()
  print 'Case #%d: %s' %(i+1, solve(b))




