def printout(n, v):
  print "Case #" + str(n) + ": " + str(v)
  
def isCorrect(arr):
  symbols = set()
  for i,j in enumerate(arr):
    for k, l in enumerate(j):
      if l != '.':
        symbols.add((l, i, k))
  for i in symbols:
    for j in symbols:
      if i != j:
        if i[1]==j[1] or i[2]==j[2]:
          if i[0] == '+' or j[0] == '+':
            pass
          else:
            print "ZLEEEE"
        if i[1]+i[2] == j[1]+j[2] or i[1]-i[2]==j[1]-j[2]:
          if i[0] == 'x' or j[0] == 'x':
            pass
          else:
            print "ZLEEEE2"
 
def call(ii):
  n, m = [int(i) for i in raw_input().split()]
  row = [' ' for i in range(n)]
  nonplus = -1
  for i in range(m):
    v, r, c = raw_input().split()
    row[int(c)-1] = v
    if v != '+':
      nonplus = int(c)-1
  res = []
  if nonplus == -1:
    nonplus = 0
    row[0] = 'o'
    res.append(('o', 0, 0))
  for i,v in enumerate(row):
    if v == ' ':
      res.append(('+', 0, i))
    elif v == 'x':
      res.append(('o', 0, i))
      nonplus = i
  for i in range(0,nonplus):
    res.append(('x', i+1, i))
  for i in range(nonplus+1, n):
    res.append(('x', i, i))
  for i in range(1,n-1):
    res.append(('+', n-1, i))
    """
  #print n, row
  s=[['.' for j in range(n)] for i in range(n)]
  s[0] = row
  for i in res:
    s[i[1]][i[2]] = i[0]
  st=''
  for i in s:
    for j in i:
      st+=j
    st+='\n'
  #print st
  
  return"""
  printout(ii, str((3*n - 2) if n != 1 else 2)+  ' '+str(len(res)))
  #isCorrect(s)
  for i in res:
    print i[0], i[1]+1, i[2]+1
  
  
  
  
t = int(raw_input())
for ii in xrange(t):
  call(ii+1)