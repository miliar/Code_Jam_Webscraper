def next(x):
 x='0'+str(x);x=list(x);x.reverse();s=''
 for m in range(1,len(x)):
  if x[m]<x[m-1]: f=m; break
 g=x[:m];j=x[m+1:];g.sort();j.reverse()
 for l in j: s+=l
 for n in range(len(g)):
  if int(g[n])>int(x[m]): s+=g[n]; g=[x[m]]+g[:n]+g[n+1:]; break
 g.sort()
 for l in g: s+=l
 return int(s)

inp=file('B-large.in').read().split('\n');inp.reverse()
out=file('B-large.out','w+')
for l in range(int(inp.pop())):
 out.write('Case #'+str(l+1)+': '+str(next(inp.pop()))+'\n')