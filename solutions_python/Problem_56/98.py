import sys

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  N,K=map(int, raw_input().split())
  t = []
  for i in range(N):
    line=raw_input().strip()
    line = line.replace('.','')
    line = '.'*(N-len(line))+line
    t.append(line)

  r=False
  b=False
  dis = [1,0,1, 1]
  djs = [0,1,1,-1]
  for u in range(4):
    di=dis[u]
    dj=djs[u]
    for i in range(N):
      if i+(K-1)*di<N:
        for j in range(N):
          if j+(K-1)*dj>=0 and j+(K-1)*dj<N:
            lr = True
            lb = True
            for k in range(K):
              lr &= t[i+k*di][j+k*dj]=='R'
              lb &= t[i+k*di][j+k*dj]=='B'
            r |= lr
            b |= lb
  res = 'Neither'
  if r and b:
    res = 'Both'
  elif r:
    res = 'Red'
  elif b:
    res = 'Blue'
  print 'Case #%s: %s'%(case_index,res)


sys.stderr.write('\n')
