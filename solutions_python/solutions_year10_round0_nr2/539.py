from math import *

def gcd(a,b):
  while b != 0:
    t = b
    b = a % b
    a = t
  return a

def solve(prob):
  f=open(prob+'.in','r')
  out=open(prob+'.out','w')
  
  C = int(f.readline())
  for c in range(C):
    V=map(int,f.readline().split())[1:]
    os=abs(V[1]-V[0])
    for i in range(2,len(V)):
      os=gcd(os,abs(V[i]-V[i-1]))
    ad=V[0]%os
    if ad > 0: ad = os-ad
    print >>out,'Case #%d: %s'%(c+1,ad)

  f.close()

#  for x in result
  out.close()

#solve(sys.argv[1])
#for i in range(1,11): solve(i)
solve('B-large')