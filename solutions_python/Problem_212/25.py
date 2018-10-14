from sys import stdin

def getstrings(): return [x for x in stdin.readline().strip().split()]
def getints(): return [int(x) for x in stdin.readline().strip().split()]
def getfloats(): return [float(x) for x in stdin.readline().strip().split()]

def thing(N,P,G):
  NN=[0,0,0,0,0]
  for g in G: NN[g%P]+=1
  if P==2: return N-NN[1]/2
  if P==3:
    m=min(NN[1],NN[2])
    M=max(NN[1],NN[2])
    return N-m-2*(M-m)/3
  if P==4:
    if NN[1]<NN[3]: (NN[1],NN[3])=(NN[3],NN[1])
    l=[0]*NN[0]
    l+=[1,3]*NN[3]
    l+=[2]*NN[2]
    l+=[1]*(NN[1]-NN[3])
    t=0;ok=0
    for x in l:
      if t==0: ok+=1
      t=(t+x)%P
    return ok

T=int(stdin.readline())
for case in range(1,T+1):
  [N,P]=getints()
  G=getints()
  print "Case #%d:"%case,thing(N,P,G)
