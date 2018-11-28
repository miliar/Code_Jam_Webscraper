from copy import deepcopy as dc
ri = raw_input

def solve():
  K = ri()
  rows, cols = K.split()
  rows, cols = int(rows), int(cols)
  m = []
  broke = False
  for i in xrange(rows):
    l = ri()
    totb = 0
    blue, count = False, 0
    for c in l:
      if c == '#':
        totb += 1
        if not blue:
          count = 0
        count += 1
      else:
        if count%2 != 0:
          broke = True
          break
    m.append(list(l))
    if broke:
      continue
    
  if totb%4 != 0:
    broke = True
  #if broke:
  #  return '\nImpossible'
  for y in xrange(rows):
    for x in xrange(cols):
      if m[y][x] == '#':
        if y+1 < rows and x+1 < cols and '#' == m[y+1][x] == m[y][x+1] == m[y+1][x+1]:
           m[y][x] = m[y+1][x+1] = '/'
           m[y+1][x] = m[y][x+1] = '\\'
        else:
          return "\nImpossible"
  r = '\n'.join([''.join(q) for q in m])
  return '\n%s'%r
  

n = int(ri())
for i in xrange(1,n+1):
  print "Case #%d:"%i, solve()