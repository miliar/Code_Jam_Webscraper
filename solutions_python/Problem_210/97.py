import sys

def thing(L0,L1):
  L=[]
  for (a,b) in L0: L.append((a,b,0))
  for (a,b) in L1: L.append((a,b,1))
  L.sort()
  if len(L)==0: return 2
  n=len(L)
  poss={}# map from (#changeovers at t+epsilon) to list of intervals of parent 0 time
  poss[0]=[(0,0)]
  L.append((L[0][0]+1440,L[0][1]+1440,L[0][2]))
  #print;print L
  for i in range(len(L)-1):
    (a0,b0,p0)=L[i]
    (a1,b1,p1)=L[i+1]
    newposs={}
    if p0==0: iv=[b0-a0,a1-a0];x=a1-a0
    else: iv=[0,a1-b0];x=0
    for c in poss:# c = #source changeovers
      if p1!=p0: # 1 new changeover
        if c+1 not in newposs: newposs[c+1]=[]
        for (mi,mx) in poss[c]: newposs[c+1].append((mi+iv[0],mx+iv[1]))
      else: # 0 or 2 changeovers
        if c not in newposs: newposs[c]=[]
        for (mi,mx) in poss[c]: newposs[c].append((mi+x,mx+x))
        if c+2 not in newposs: newposs[c+2]=[]
        for (mi,mx) in poss[c]: newposs[c+2].append((mi+iv[0],mx+iv[1]))
    poss={}
    for c in newposs:
      l=newposs[c]
      l.sort()
      m=[]
      for [a,b] in l:
        if len(m)>0 and m[-1][1]>=a: m[-1]=[m[-1][0],max(m[-1][1],b)]
        else: m.append([a,b])
      poss[c]=m
    #print poss;print
  #print
  #for c in poss: print c,poss[c]
  for c in sorted(list(poss)):
    for (mi,mx) in poss[c]:
      if mi<=720 and mx>=720: return c
  return "IMPOSSIBLE"
    

T=int(sys.stdin.readline())
for case in range(1,T+1):
  [AC,AJ]=[int(y) for y in sys.stdin.readline().strip().split()]
  L0=[[int(y) for y in sys.stdin.readline().strip().split()] for i in range(AC)]
  L1=[[int(y) for y in sys.stdin.readline().strip().split()] for i in range(AJ)]
  print "Case #%d:"%case,thing(L0,L1)
