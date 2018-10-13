import sys

input = sys.stdin
T = int(input.readline())

def calc(data, _r, _c):
  dd = [(0,0), (1,0), (0,1), (1,1)]
  for i in xrange(_r):
      for j in xrange(_c):
        if d[i][j] == '#':
          for ddd in dd:
            if not (0 <= i + ddd[0] < _r and 0 <= j+ddd[1] < _c) or d[i+ddd[0]][j+ddd[1]] != '#':
              return 'Impossible'
          else:
            for ddd in dd:
              d[i][j] = '/'
              d[i][j+1] = '\\'
              d[i+1][j] = '\\'
              d[i+1][j+1] = '/'
  return None

for t in xrange(T):
  R, C = map(int, input.readline().strip().split(' '))
  d = [ list(input.readline().strip()) for i in xrange(R)] 

  ret = calc(d, R, C)
  print 'Case #%d:'%(t+1)
  if ret:
    print ret
  else:
    for l in d:
      print ''.join(l)

  
