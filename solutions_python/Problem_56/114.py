#!/usr/bin/python
import sys

def valid(x,y,N):
  return ((x>=0) and (x<N) and (y>=0) and (y<N))

def add(score,table,x,y,N):
  maxB=0
  maxR=0
  c=table[x,y]
  score[x,y]=dict()
  for dir in [ (-1,0),(-1,-1), (0,-1), (-1,1) ]:
    nx=x+dir[0]
    ny=y+dir[1]
    if valid(nx,ny,N):
      if table[nx,ny]==c:
        if (nx,ny) in score:
          if dir in score[nx,ny]:
            score[x,y][dir]=score[nx,ny][dir]+1
          else:
            score[x,y][dir]=2
        else:
          score[x,y][dir]=2
        if score[x,y][dir]>maxR and c=='R':
          maxR=score[x,y][dir] 
        if score[x,y][dir]>maxB and c=='B':
          maxB=score[x,y][dir] 
  return (maxB,maxR)

def printtable(table,N):
  for y in range(N):
    for x in range(N):
      print table[x,y],
    print ""

f = open(sys.argv[1],'r')
n = int(f.readline())
for tc in range(1,n+1):
  line=f.readline().rstrip('\n').split(" ")
  N=int(line[0])
  K=int(line[1])
  table=dict()
  for i in range(N):
    row=f.readline().rstrip('\n')
    for j in range(len(row)): 
#rotate
      x=N-1-i
      y=j
      table[x,y]=row[j]
#  print "rotate"
#  printtable(table,N)
#gravity
  for x in range(N):
    for y in range(N-1,-1,-1):
      if table[x,y]!='.':
        i=1
        while (valid(x,y+i,N) and table[x,y+i]=='.'):
          i=i+1
        if table[x,y+i-1]=='.':
          table[x,y+i-1]=table[x,y]
          table[x,y]='.'
#score
#  print "gravity"
#  printtable(table,N)
  score=dict()
  maxR=0
  maxB=0
  for x in range(N):
    for y in range(N):
        (nB,nR)=add(score,table,x,y,N)
        if (nB>maxB):
          maxB=nB
        if (nR>maxR):
          maxR=nR
#  print (maxB,maxR)
  if maxR>=K and maxB>=K:
    Result="Both"
  elif maxR>=K:
    Result="Red"
  elif maxB>=K:
    Result="Blue"
  else:
    Result="Neither"
  print "Case #%d: %s"%(tc,Result)
