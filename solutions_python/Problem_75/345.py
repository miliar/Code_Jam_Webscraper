#!/usr/bin/python
import sys
import subprocess

TC=0
DEBUG=False
if len(sys.argv)>2:
  DEBUG=True
  TC=int(sys.argv[2])

def debugprint(s,t):
  if DEBUG and(t==TC):
      print s

def qadd(Q,key,value):
  if key in Q:
    Q[key].append(value)
  else:
    Q[key]=[value]

input = open (sys.argv[1],'r')
T = int(input.readline())
for t in range(0,T):
  S = []
  D = dict()
  C = dict()
  X = input.readline().rstrip().split(' ')
  debugprint(X,t)
  ps = int (X[0])
  pps = int (X[ps+1])+ps+1
  Q = X[pps+2]
  #combine
  for i in range(0,ps):
    first = X[i+1][0]
    second = X[i+1][1]
    comb = X[i+1][2]
    if (first in C):
      C[first][second]=comb
    else:
      C[first]=dict({second:comb})
    if (second in C):
      C[second][first]=comb
    else:
      C[second]=dict({first:comb})
  debugprint(C,t)
  #remove
  for j in range(ps+1,pps):
    first = X[j+1][0]
    second = X[j+1][1]
    qadd(D,first,second)
    qadd(D,second,first)
  debugprint(D,t)
  i = 1
  S = [ Q[0] ]
  q = None
  while (i<len(Q) or q != None):
    next=True
    if q == None:
      q = Q[i]
    debugprint(("%d "%i)+q,t)
    debugprint(S,t)
    if q in C:
      if len(S)>0 and S[-1] in C[q]:
        top = S.pop()
        q = C[q][top]
        next=False
    if q in D:
      for o in D[q]:
        if o in S:
          S = []
          q = None
          break
    if next:
      if q!=None:
        S.append(q)
      q=None
      i = i+1
  print "Case #%d:" % (t+1),
  QQ=""
  if len(S)>0:
    QQ=S[0]
  for i in range(1,len(S)):
    QQ=QQ+", "+S[i]
  print "["+QQ+"]"

