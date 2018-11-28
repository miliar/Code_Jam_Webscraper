import sys
INF = 10000

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  n,m = map(int,raw_input().split())
  r = [-1 for i in range(n)]
  c = [-1 for i in range(m)]
  a = []
  for i in range(n):
    a.append(map(int,raw_input().split()))
    for j in range(m):
      r[i] = max(r[i],a[i][j])
      c[j] = max(c[j],a[i][j])
  b = [[INF]*m for i in range(n)]
  for i in range(n):
    for j in range(m):
      b[i][j] = min(r[i],c[j])
  res = 'YES'
  for i in range(n):
    for j in range(m):
      if a[i][j]!=b[i][j]:
        res = 'NO'
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')

