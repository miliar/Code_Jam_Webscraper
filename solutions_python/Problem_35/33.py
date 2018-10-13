
import sys

di=[-1,0,0,1]
dj=[0,-1,1,0]

def flow(i,j):
  global h,w,m,memo,bassin
  if not memo[i][j]=='':
    return memo[i][j]
  lowest=m[i][j]
  for dir in range(4):
    ii=i+di[dir]
    jj=j+dj[dir]
    if ii>=0 and ii<h and jj>=0 and jj<w:
      if m[ii][jj]<lowest:
        lowest=m[ii][jj]
        iii=ii
        jjj=jj
  if lowest<m[i][j]:
    res=flow(iii,jjj)
  else:
    res=chr(ord('a')+bassin)
    bassin+=1
  memo[i][j]=res
  return res

for case_index in range(1, 1+input()):

  global h,w,m,memo,bassin
  sys.stderr.write(str(case_index)+' ')  
  h,w=map(int,raw_input().split())
  m = []
  for i in range(h):
    m.append(map(int,raw_input().split()))
  bassin=0
  memo = []
  for i in range(h):
    memo.append([''for j in range(w)])
  print 'Case #'+str(case_index)+':'
  for i in range(h):
    line=[]
    for j in range(w):
      line += flow(i,j)
    print ' '.join(line)

sys.stderr.write('\n')
