def check(t,k,n):
  red = False
  blue = False
  #hori
  for x in t:
    if 'R'*k in x: red = True
    if 'B'*k in x: blue = True
  #ver
  for i in range(n):
    x = ''
    for j in range(n):
      x += t[j][i] 
    if 'R'*k in x: red = True
    if 'B'*k in x: blue = True

  rows = range(n)
  #dia1
  for i in range(n):
    x = ''
    for j in range(n-i):
      x += t[i+j][j]
    #print s
    #raw_input('con')
    if 'R'*k in x: red = True
    if 'B'*k in x: blue = True
    #print 'bool',red,blue

  #dia2
  for i in range(n):
    x = ''
    for j in range(n-i):
      x += t[j][i+j]
    #print s
    #raw_input('con2')
    if 'R'*k in x: red = True
    if 'B'*k in x: blue = True
     
  #dia3
  for i in range(n):
    x = ''
    for j in range(n-i):
      x += t[n-1-j-i][j]
    #print s
    #raw_input('con3')
    if 'R'*k in x: red = True
    if 'B'*k in x: blue = True

  #dia4
  for i in range(n):
    x = ''
    for j in range(n-i):
      x += t[j][n-1-j-i]
    #print s
    #raw_input('con4')
    if 'R'*k in x: red = True
    if 'B'*k in x: blue = True

  return (red,blue)
if __name__ == '__main__':
  #f = open('test.txt')
  f = open('Downloads/A-small-attempt0.in')
  case = int(f.readline().strip())
  for i in xrange(1,case+1):
  #for i in xrange(1,2):
    n, k = [int(x) for x in f.readline().strip().split()]
    table = []
    r_table = []
    g_table = []
    #table
    for j in xrange(n):
      t = filter(lambda x: x != '.', f.readline().strip())
      t = '.'*(n-len(t)) + ''.join(t)
      table.append(t)

    #rotate
    for j in xrange(n):
      r_table.append('')
      for l in xrange(n):
        r_table[j] += table[n-l-1][j]
      
    #for x in r_table: print x
    #check
    red,blue = check(r_table,k,n)
    #print red,blue
    if red and blue : print 'Case #%d:'%i,'Both'
    elif not red and blue : print 'Case #%d:'%i,'Blue'
    elif red and not blue : print 'Case #%d:'%i,'Red'
    elif not red and not blue : print 'Case #%d:'%i,'Neither'
