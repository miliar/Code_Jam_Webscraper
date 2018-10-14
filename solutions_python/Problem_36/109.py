inp=file('C-large.in').read().split('\n')

def sol(a):
 b=''
 for l in a: b+=['',l][l in 'welcome to code jam']
 b=list(b);c=[0]*len(b);d=[0]*len(b)
 for l in range(len(b)):
  if b[l]=='m': c[l]+=1
 for x in 'aj edoc ot emoclew':
  for l in range(len(b)):
   if b[l]==x: d[l]+=sum(c[l+1:])%10000
  c,d=d,[0]*len(b)
 return str(sum(c)%10000).zfill(4)

out=file('C-large.out','w+')
for l in range(1,int(inp[0])+1):
 out.write('Case #'+str(l)+': '+sol(inp[l])+'\n')