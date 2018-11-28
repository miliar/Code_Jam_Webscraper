def decide(t, N, M):
  hmax = [0]*N
  vmax = [0]*M
  for i in range(N):
    hmax[i] = t[i][0]
    for j in range(M):
      if t[i][j] > hmax[i]:
        hmax[i] = t[i][j]
  for j in range(M):
    vmax[j] = t[0][j]
    for i in range(N):
      if t[i][j] > vmax[j]:
        vmax[j] = t[i][j]
  for i in range(N):
    for j in range(M):
      if t[i][j] != hmax[i] and t[i][j] != vmax[j]:
        return 'NO'
  return 'YES'
  
     

def solve():
#  f = open("in.txt", 'r')
#  f = open("B-small-attempt0.in")
  f = open("B-large.in")
  T = int(f.readline())
  for i in range(T):
    l = f.readline()
    [N, M] = [int(k) for k in l.split()]
    t = [[]]*N
    for j in range(N):
      l = f.readline()
      t[j] = [int(k) for k in l.split()]
    print "Case #%i:" % (i+1), decide(t, N, M)

solve()

