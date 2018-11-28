#!/usr/bin/python2
from sys import stdin



C = int(stdin.readline())

for c in range(1,C+1):
  
  t = stdin.readline().split()
  y,x=int(t[0]),int(t[1])
  p=[]
  for i in range(0,y):
    p.append(list(stdin.readline()[:-1]))
  #print p,x,y
  for y_ in range(0,y):
    for x_ in range(0,x):
      #print x_,y_,p[1][1]
      if(x_<x-1 and y_<y-1 and p[y_][x_]=="#" and p[y_][x_+1]=="#" and p[y_+1][x_]=="#" and p[y_+1][x_+1]=="#"):
        p[y_][x_]="/"
        p[y_][x_+1]="\\"
        p[y_+1][x_]="\\"
        p[y_+1][x_+1]="/"
  #print p
  s=""
  for l in p:
    #if(c==8): print l
    if(len(s)>0 and s[0]=="I"): break
    for ch in l:
      if(ch=="#"):
        s="Impossible"
        break
      s+=ch
    s+="\n"
  print "Case #%d:" % c
  print s,
  
  
