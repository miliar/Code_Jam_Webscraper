f = open('A-large.in', 'r')
ff = open('A-large.out', 'w')

t = int(f.readline())
for tt in range(t):
  r,c = f.readline().split(' ')
  r = int(r)
  c = int(c)
  m = []
  for i in range(r):
    m.append(list(f.readline().strip()))
  for i in range(r):
    lc='?'
    for j in range(c):
      if m[i][j] == '?':
        m[i][j] = lc
      else:
        lc = m[i][j]
  for i in range(r):
    lc='?'
    for j in range(c - 1, -1, -1):
      if m[i][j] == '?':
        m[i][j] = lc
      else:
        lc = m[i][j]

  for i in range(1, r, 1):
    if m[i][0] == '?':
      m[i] = m[i-1]

  for i in range(r - 2, -1, -1):
    if m[i][0] == '?':
      m[i] = m[i+1]

  ff.write('Case #' + str(tt+1) + ':\n')
  for i in m:
    ff.write(''.join(i) + '\n')
