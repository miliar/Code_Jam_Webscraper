import sys
#f=open('input');
f=sys.stdin;
g=sys.stdout;
x=f.readline();N=int(x.strip());
for iN in range(1,N+1):
  x=f.readline();nS=int(x.strip());
  #read search engines
  s={};sk=[];
  for i in range(nS):
    x=f.readline().strip();
    s[x]=0;sk.append(x);
  #read queries
  x=f.readline();nQ=int(x.strip());
  mS=nS;# num of corrent active engines
  nSwith=0;
  for i in range(nQ):
    x=f.readline().strip();
    if s[x]==0:#active
      s[x]=1;mS-=1;
    if mS==0:#switch
      nSwith+=1; mS=nS;
      for t in sk:s[t]=0;
      #x is disabled
      s[x]=1;mS-=1;
  #output
  g.write('Case #%d: %d\n'%(iN,nSwith));
f.close();g.close();
    
    
  
    
  
    
