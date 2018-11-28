#!/usr/bin/python

def isRecycleable(n,m):
  a = str(n)
  b = str(m)
  if len(a)!=len(b):
    return 0
  for i in range(0,len(a)):
    if a.startswith(b[i:]) and a.endswith(b[0:i]):
      return 1
  return 0

def compute():
  s = raw_input().split()
  a = int(s[0])
  b = int(s[1])
  count=0
  for i in range(a,b):
    for j in range(i+1,b+1):
      count+=isRecycleable(i,j)
  return count

n = int(raw_input())
for i in range(0,n):
  print "Case #%d: "%(i+1)+str(compute())
