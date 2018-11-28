import sys
def read_values():
  return map(int,raw_input().split())

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  R,C,D = read_values()
  m = []
  for i in range(R):
    m.append(map(int,list(raw_input().strip())))

  c = [[[0,0] for j in range(C+1)] for i in range(R+1)]
  for i in range(R):
    s = [0,0]
    for j in range(C):
      s[0] += i*m[i][j]
      s[1] += j*m[i][j]
      c[i+1][j+1] = [c[i][j+1][0]+s[0],c[i][j+1][1]+s[1]]
  
  a = [[0 for j in range(C+1)] for i in range(R+1)]
  for i in range(R):
    s = 0
    for j in range(C):
      s += m[i][j]
      a[i+1][j+1] = a[i][j+1]+s

  res = -1
  for K in range(3,min(R,C)+1):
    for i in range(K-1,R):
      for j in range(K-1,C):
        s = [0,0]
        s[0] = c[i+1][j+1][0]
        s[1] = c[i+1][j+1][1]
        s[0] -= c[i+1-K][j+1][0]
        s[1] -= c[i+1-K][j+1][1]
        s[0] -= c[i+1][j+1-K][0]
        s[1] -= c[i+1][j+1-K][1]
        s[0] += c[i+1-K][j+1-K][0]
        s[1] += c[i+1-K][j+1-K][1]
        
        s[0] -= i*m[i][j]
        s[1] -= j*m[i][j]
        s[0] -= (i-K+1)*m[i-K+1][j]
        s[1] -=       j*m[i-K+1][j]
        s[0] -=       i*m[i][j-K+1]
        s[1] -= (j-K+1)*m[i][j-K+1]
        s[0] -= (i-K+1)*m[i-K+1][j-K+1]
        s[1] -= (j-K+1)*m[i-K+1][j-K+1]

        total = a[i+1][j+1]
        total -= a[i+1-K][j+1]
        total -= a[i+1][j+1-K]
        total += a[i+1-K][j+1-K]

        total -= m[i][j]
        total -= m[i-K+1][j]
        total -= m[i][j-K+1]
        total -= m[i-K+1][j-K+1]

        if 2*s[0] == total*(2*i-(K-1)) and 2*s[1] == total*(2*j-(K-1)):
          if K>res:
            res = K
  if res == -1: res = 'IMPOSSIBLE'
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
