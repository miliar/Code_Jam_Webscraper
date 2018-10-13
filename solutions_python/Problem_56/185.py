#!/usr/bin/python

#fi = open("A-test.in", "r")
fi = open("A-small-attempt0.in", "r")
#fi = open("A-large-practice.in", "r")
#fo = open("A-test.out", "w")
fo = open("A-small-attempt0.out", "w")
#o = open("A-large-practice.out", "w")

FOUND=[False,False]

C=[]
C1=[]
N,K='0','0'

def check_r(c,y,x):
  global N,K
  global C, C1
  global FOUND 

  check=C[y][x]

  cnt = 0

  for i in xrange(int(K)):
    if x+i >= int(N):
      break
    C1[c][y][x+i]+=1
    if C[y][x+i] == check:
      cnt+=1
  
  if cnt == int(K):  
      FOUND[c]=True

def check_c(c,y,x):
  global N,K
  global C, C1
  global FOUND 

  check=C[y][x]

  cnt = 0

  for i in xrange(int(K)):
    if y+i >= int(N):
      break
    C1[c][y+i][x]+=2
    if C[y+i][x] == check:
      cnt+=1
  
  if cnt == int(K):  
      FOUND[c]=True

def check_x1(c,y,x):
  global N,K
  global C, C1
  global FOUND 

  check=C[y][x]

  cnt = 0

  for i in xrange(int(K)):
    if y+i >= int(N):
      break
    if x+i >= int(N):
      break
    C1[c][y+i][x+i]+=4
    if C[y+i][x+i] == check:
      cnt+=1
  
  if cnt == int(K):  
      FOUND[c]=True

def check_x2(c,y,x):
  global N,K
  global C, C1
  global FOUND 

  check=C[y][x]

  cnt = 0

  for i in xrange(int(K)):
    if y+i >= int(N):
      break
    if x-i < 0:
      break
    C1[c][y+i][x-i]+=8
    if C[y+i][x-i] == check:
      cnt+=1
  
  if cnt == int(K):  
      FOUND[c]=True


T = int(fi.readline().strip())

for Cases in xrange(1,T+1):

  N,K=fi.readline().strip().split()

  print N,K

  FOUND=[False,False]

  B=[]
  C=[]
  C1=[[],[]]

  for i in xrange(int(N)):
    B.append(fi.readline().strip())

  for i in xrange(int(N)):
    C.append([])
    C1[0].append([])
    C1[1].append([])
    for j in xrange(int(N)):
      C[i].append('.')
      C1[0][i].append(0)
      C1[1][i].append(0)

  cnti=0
  cntj=0

  for i in xrange(int(N)):
    modified=False
    for j in xrange(int(N)):
      if B[int(N)-1-i][int(N)-1-j]!='.':
        C[cnti][cntj]=B[int(N)-1-i][int(N)-1-j]
        modified=True
        cntj=(cntj+1)
    cntj=0
    if modified:
      cnti+=1

  for i in xrange(int(N)):
    for j in xrange(int(N)):
      c=0
      if C[i][j]=='B':
        c=1
      elif C[i][j]=='R':
        c=0
      else:
        continue

      if FOUND[c] == True:
        continue

      if C1[c][i][j]&1 == 0:
        check_r(c,i,j)
      if C1[c][i][j]&2 == 0:
        check_c(c,i,j)
      if C1[c][i][j]&4 == 0:
        check_x1(c,i,j)
      if C1[c][i][j]&8 == 0:
        check_x2(c,i,j)

  for i in xrange(int(N)):
    print C[i]

  print FOUND

  output=''
  if FOUND[0]==True and FOUND[1]==True:
    output='Both'
  elif FOUND[0]==True and FOUND[1]==False:
    output='Red'
  if FOUND[0]==False and FOUND[1]==True:
    output='Blue'
  if FOUND[0]==False and FOUND[1]==False:
    output='Neither'

  print 'Case #%d: %s' % (Cases, output)
  fo.writelines('Case #%d: %s\n' % (Cases, output))

fi.close()
fo.close()
