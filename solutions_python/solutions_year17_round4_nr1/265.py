def sol(P,G):
 L=[0]*P
 while G: L[G.pop()%P]+=1
 if P==2: out=L[0]; r=L[1]/2; out+=r; L[1]-=r*2; out+=L[1]>0; return out
 if P==3:
  out=L[0]; L[0]=0; t=min(L[1],L[2]); out+=t; L[1]-=t; L[2]-=t
  r=(L[1]+L[2])/3; out+=r; out+=(L[1]+L[2]-3*r)>0
  return out
 if P==4:
  out=L[0]; L[0]=0; t=min(L[1],L[3]); out+=t; L[1]-=t; L[3]-=t
  r=L[2]/2; out+=r; L[2]-=2*r
  s=min(L[1]/2,L[2]); out+=s; L[1]-=2*s; L[2]-=s
  q=min(L[2],L[3]/2); out+=q; L[2]-=q; L[3]-=2*q
  u=(L[1]+L[3])/4; out+=u; out+=(L[1]+L[3]-4*u)>0
  return out

inp=file('A-small-attempt0.in','rb+'); out=file('A-small-attempt0.out','wb+')
for t in range(1,int(inp.readline().strip())+1):
 N,P=inp.readline().strip().split(' '); N=int(N); P=int(P)
 G=[int(i) for i in inp.readline().strip().split(' ')]
 #print sol(P,G)
 out.write('Case #%i: %i\r\n'%(t,sol(P,G)))