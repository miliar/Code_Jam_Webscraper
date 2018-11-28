import sys
#f=open('example.in');
f=sys.stdin;
g=sys.stdout
x=f.readline();N=int(x.strip());

def fNext(p,ip):
  if ip<0:return [];
  S=len(p);
  #tR : non-appear in p[:ip]
  tR=range(S);
  for p1 in p[:ip]:tR[p1]=-1;
  #find mininum t in tR that t>p[ip];
  for i in range(S):
    if tR[i]>=0 and i>p[ip]:break;
  if not (tR[i]>=0 and i>p[ip]): return fNext(p,ip-1);
  p[ip]=i;tR[i]=-1;
  #fill the rest
  i0=ip+1;
  for it in range(S):
    if tR[it]>=0:p[i0]=it;i0+=1;
  return p


for iN in range(1,N+1):
  t=f.readline();  k=int(t);
  t=f.readline();  s=t.strip();
  
  p=[];ND=[];
  for i in range(k):p.append(i);
  while 1:
    u='';
    for i in range(0,len(s),k):
      tu='';
      for p1 in p:
        tu+=s[i+p1];
      u+=tu;
    
    #decompass
    n=0;
    for i in range(len(u)-1):
      if u[i+1]!=u[i]:n+=1;
    ND.append(n);
    
    p=fNext(p,len(p)-1);
    if p==[]:break;
  n=min(ND)+1;
  g.write('Case #%d: %d\n'%(iN,n));
f.close();g.close();
      
    
    
  
    
    
  
  
  
