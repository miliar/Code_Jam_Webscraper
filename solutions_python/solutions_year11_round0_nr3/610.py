#!/usr/bin/python2
from sys import stdin

def split(x,y,x_,y_,ar):
  if(ar!=[]):
    a=split(x^ar[0],y,x_+ar[0],y_,ar[1:])
    b=split(x,y^ar[0],x_,y_+ar[0],ar[1:])
    if(a>b): return a
    else: return b
  else:
    if(x==y and x_>=y_ and y_!=0):
      return x_
    else: return -1
  
          


C = int(stdin.readline())
for case in range(1,C+1):
  i = int(stdin.readline())
  t = map(int,stdin.readline().split())
  #t = stdin.readline().split()
  s=split(0,0,0,0,t)
  print "Case #%d:" % case,
  if(s==-1):
    print "NO"
  else:
    print s
