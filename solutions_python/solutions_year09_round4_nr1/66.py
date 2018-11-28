
import sys

for case_index in range(1, 1+input()):

  sys.stderr.write(str(case_index)+' ')
  N=input()
  M=[]
  for _ in range(N):
    M.append(map(int, list(raw_input())))
  u=[]
  for i in range(N):
    a = N-1
    for j in range(N-1,-1,-1):
      if M[i][j]==1:
        break
      a -= 1
    u.append(a)
  res = 0
  for i in range(N):
    if u[i]>i:
      j=i
      while u[j]>i:
        j+=1
      while i<j:
        x = u[j-1]
        u[j-1]=u[j]
        u[j]=x
        j-=1
        res+=1

  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
