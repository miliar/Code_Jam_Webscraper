#!/usr/bin/python

import math  

def solve():
  [A,B] = map(int, f.pop(0).split())
  c = 0 
  for i in T:
    if i>=A and i<=B: c+=1
  return c
  
def pal(n):
  n = str(n)
  for i in range(len(n)/2):
    if not n[i]==n[len(n)-1-i]: 
      return False
  else: return True 
  
infile=open("C-large-1.in",'r')
f=map(lambda s:s.strip(),infile.readlines())
infile.close()

N = int(f.pop(0))
x = int(math.sqrt(10**14))+1
T = []
for i in range(x):
  if pal(i):
    if pal(i**2): 
      T.append(i**2)
print T

out=open("C-large-1-result",'w')
for n in range(N):
  out.write("Case #%s: %s\n"%(n+1, solve()))
out.close()