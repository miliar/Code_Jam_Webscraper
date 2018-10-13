import sys

def thing(D,N,horses):
  tmax=0.
  for [K,S] in horses:
    t=(D-K)/float(S)
    tmax=max(t,tmax)
  return D/tmax

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [D,N]=[int(y) for y in sys.stdin.readline().strip().split()]
  horses=[]
  for i in range(N):
    horses.append([int(y) for y in sys.stdin.readline().strip().split()])
  print "Case #%d:"%case,thing(D,N,horses)
