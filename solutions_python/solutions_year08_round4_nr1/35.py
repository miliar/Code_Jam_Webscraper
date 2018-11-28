import sys
#f=open('example.in');
f=sys.stdin;
gFile=sys.stdout
x=f.readline();N=int(x.strip());
global RES;

def fChange(X,OP,C,k,v):
  res=-1;
  if RES[k][v]>=-1:res=RES[k][v];
  elif X[k]==v:res=0;
  elif k>=len(OP):res=-1;
  else:
    x1=X[2*k+1];x2=X[2*k+2];res=-1;
    if (OP[k]==1 and v==1)or(OP[k]==0 and v==0):
      n1=fChange(X,OP,C,2*k+1,v);
      n2=fChange(X,OP,C,2*k+2,v);
      if n1>=0 and n2>=0:res=n1+n2;
    elif (OP[k]==1 and v==0)or(OP[k]==0 and v==1): 
      n1=fChange(X,OP,C,2*k+1,v);
      n2=fChange(X,OP,C,2*k+2,v);
      if n1>=0 or n2>=0:
        if n1<0:tn=n2
        elif n2<0:tn=n1
        else: tn=min([n1,n2]);
        res=tn;
    
    res2=-1;
    if C[k]==1:
      op2=1-OP[k];
      if (op2==1 and v==1)or(op2==0 and v==0):
        n1=fChange(X,OP,C,2*k+1,v);
        n2=fChange(X,OP,C,2*k+2,v);
        if n1>=0 and n2>=0:res2=n1+n2+1;
      elif(op2==1 and v==0)or(op2==0 and v==1): 
        n1=fChange(X,OP,C,2*k+1,v);
        n2=fChange(X,OP,C,2*k+2,v);
        if n1>=0 or n2>=0:
          if n1<0:tn=n2
          elif n2<0:tn=n1
          else: tn=min([n1,n2]);
          res2=tn+1;
    if res2>=0:
      if res<0:res=res2
      elif res2<res:res=res2
  RES[k][v]=res;
  return res;
        

      
      

  
  


for iN in range(1,N+1):
  t=f.readline().split();
  M=int(t[0]); V=int(t[1]);X=[];OP=[];C=[];
  for i in range(M):
    t=f.readline().split();
    if i<(M-1)/2:
      g=int(t[0]); c=int(t[1]);
      X.append(-1);OP.append(g);C.append(c)
    else:
      g=int(t[0])
      X.append(g);
  #
  RES=[];
  for i in range(M):
    RES.append([-2,-2]);
  #compute the tree
  for k in range( (M-1)/2-1,-1,-1):
    k1=2*k+1; k2=2*k+2;
    x1=X[k1]; x2=X[k2];
    if OP[k]==1:X[k]=x1&x2
    else:X[k]=x1|x2;
  
  #change
  n=fChange(X,OP,C,0,V);
  if n>=0:
    gFile.write('Case #%d: %d\n'%(iN,n))
  else:
    gFile.write('Case #%d: IMPOSSIBLE\n'%iN)
f.close();gFile.close();
  
    
  

