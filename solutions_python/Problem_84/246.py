#!/usr/bin/python
import math
import sys

TC=0
DEBUG=False
if len(sys.argv)>2:
  DEBUG=True
  TC=int(sys.argv[2])

def debugprint(s,t):
  if DEBUG and(t==TC):
    print s

def valid(N,M,x,y):
  return (x<N and y<M)

def get(S,N,x,y):
  return S[y*N+x]

def set(S,N,x,y,v):
  S[y*N+x]=v

def tileprint(S,X,Y):
  Q=""
  for j in range(0,Y):
    for i in range(0,X): 
      Q+=S[i+j*X]
    Q+="\n"
  return Q.rstrip() 


input = open (sys.argv[1],'r')
T = int(input.readline())
for t in range(0,T):
  R = map(int,input.readline().rstrip().split(' '))
  Q=[]
  Y=R[0]
  X=R[1]
  for r in range(0,Y):
    Q.extend(map(lambda x:x,input.readline().rstrip()));
#  print len(Q)
#  print Q
  S=""
#  tileprint(Q,X,Y)
  for j in range(0,Y):
    for i in range(0,X):
      if (get(Q,X,i,j)=='#'):
        set(Q,X,i,j,'/')
        if valid(X,Y,i+1,j) and get(Q,X,i+1,j)=='#':
          set(Q,X,i+1,j,'\\')
        else:
          S="Impossible" 
          break
        if valid(X,Y,i,j+1) and get(Q,X,i,j+1)=='#':
          set(Q,X,i,j+1,'\\')
        else:
          S="Impossible" 
          break
        if valid(X,Y,i+1,j+1) and get(Q,X,i+1,j+1)=='#':
          set(Q,X,i+1,j+1,'/')
        else:
          S="Impossible" 
          break
  if (S!="Impossible"):
    S=tileprint(Q,X,Y)
  print "Case #%d:\n%s" % (t+1,S)

