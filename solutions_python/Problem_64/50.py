#!/usr/bin/python
import sys

def printtable(table,N,M):
  for y in range(M):
    for x in range(N):
      print table[x,y],
    print ""

def valid(x,y,N,M):
  return (x>=0 and x<N and y>=0 and y<M)

def check(table,N,M,x,y,S):
  if not valid(x+S-1,y+S-1,N,M):
    return False
  s=table[x,y]
  for j in range(S):
    for i in range(S):
      if table[x+i,y+j]=='C':
        return False
      if (i%2==j%2):
        if table[x+i,y+j]!=s:
          return False
      else:
        if table[x+i,y+j]==s:
          return False
  return 1

HexABC="0123456789ABCDEF"

f = open(sys.argv[1],'r')
n = int(f.readline())
for tc in range(1,n+1):
  line=f.readline().rstrip('\n').split(" ")
  M=int(line[0])
  N=int(line[1])
  table=dict()
  for y in range(M):
    row=f.readline().rstrip('\n')
    for i in range(len(row)):
      c=HexABC.find(row[i])
      for d in range(4):
        x=i*4+d
        if ((2**(3-d)) & c)!=0:
          pixel='X'
        else:
          pixel=0
        table[x,y]=pixel
#  printtable(table,N,M) 
  cut=dict()
  S=min(M,N)
  while (S>0):
    for y in range(M):
      x=0
      while (x<N):
        if table[x,y]!='C':
          if check(table,N,M,x,y,S):
            #            if False:
            #  print "before:"
            #  printtable(table,N,M)
            for q in range(S):
              for u in range(S):
                table[x+q,y+u]='C'
            #if 1:
            #  print "after:"
            #  printtable(table,N,M)
            if S in cut:
              cut[S]=cut[S]+1
            else:
              cut[S]=1
        x=x+1
    S=S-1
  print "Case #%d: %s"%(tc,len(cut))
  for a in reversed(sorted(cut.keys())):
    print a,cut[a]
