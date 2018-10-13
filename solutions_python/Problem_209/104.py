import sys
from math import pi

def thing(N,K,pan):
  pan.sort()
  best=[0]*(K+1)
  gb=0
  for i in range(N):
    newbest=[0]*(K+1)
    a=2*pan[i][0]*pan[i][1]
    for j in range(K):
      newbest[j+1]=max(best[j+1],best[j]+a)
    gb=max(gb,best[K-1]+a+pan[i][0]**2)
    #print best,newbest,gb
    best=newbest
  return gb*pi

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [N,K]=[int(y) for y in sys.stdin.readline().strip().split()]
  pan=[tuple([int(y) for y in sys.stdin.readline().strip().split()]) for i in range(N)]
  print "Case #%d:"%case,thing(N,K,pan)
