#!/usr/bin/python

def solve():
  r,t = map(int,f.pop(0).split())
  n = 0
  while(t>=0):
    n += 1
    s = 2*r+4*n-3 
    if t-s>=0:
      t=t-s
    else: return n-1
    
infile=open("A-small-attempt0.in",'r')
f=map(lambda x:x.strip(),infile.readlines())
infile.close()
T=int(f.pop(0))
for t in xrange(T):
  print "Case #" + str(t + 1) + ": " + str(solve())