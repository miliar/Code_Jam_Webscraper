import sys
#f=open('example.in');
f=sys.stdin;
g=sys.stdout
x=f.readline();N=int(x.strip());

for iN in range(1,N+1):
  x=f.readline().strip();n=int(x);
  t=f.readline().split();u=[];
  for t1 in t:u.append(int(t1))
  x=u
  t=f.readline().split();u=[];
  for t1 in t:u.append(int(t1))
  y=u
  
  x.sort();y.sort();y.reverse();
  z=0;
  for i in range(n):
    z+=x[i]*y[i];
  g.write('Case #%d: %d\n'%(iN,z));
f.close();g.close();
