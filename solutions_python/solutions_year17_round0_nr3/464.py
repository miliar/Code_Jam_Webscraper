import math

def sol(N,K):
 options=[(N,1)]
 while K>sum([num for (size,num) in options]):
  K-=sum([num for (size,num) in options])
  remoptions=[]
  for (opsize,opnum) in options:
   remoptions.append(((opsize-1)-(opsize-1)/2,opnum))
   remoptions.append(((opsize-1)/2,opnum))
  remoptdict={}
  while remoptions:
   cursize,curnum=remoptions.pop(0)
   if cursize in remoptdict: remoptdict[cursize]+=curnum
   else: remoptdict[cursize]=curnum
  options=sorted([(x,remoptdict[x]) for x in remoptdict],reverse=True)
 while K>options[0][1]: K-=options[0][1]; t=options.pop(0)
 size=options[0][0]
 return ((size-1)-(size-1)/2,(size-1)/2)

inp=file('C-large.in','rb+'); out=file('C-large.out','wb+')
for t in range(1,int(inp.readline().strip())+1):
 N,K=inp.readline().strip().split(' '); N=int(N); K=int(K); y,z=sol(N,K)
 out.write('Case #%i: %i %i\r\n'%(t,y,z))