#!/usr/bin/python

def decomp(n):
  a = n/3
  b = n%3
  return ([a+1]*b)+([a]*(3-b))

def isUpgradable(l):
  return l[0]!=0 and l[0]==l[1]

def compute():
  s = raw_input()
  l = map(int,s.split())
  n = l[0]
  s = l[1]
  p = l[2]
  l = l[3:]
  ret = 0
  for i in l:
    k = decomp(i)
    if max(k) >=p:
      ret+=1
    elif s>0 and isUpgradable(k) and max(k)+1==p:
      ret+=1
      s-=1
  return ret

n = int(raw_input())
for i in range(0,n):
  print "Case #%d: "%(i+1)+str(compute())
