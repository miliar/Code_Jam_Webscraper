def answer(N,K):

 A=sorted(N+K); B=''.join([('N' if b in N else 'K') for b in A][::-1])

 Kwins=0; Kwinners=0
 for i in B:
  if i=='K': Kwinners+=1
  elif i=='N' and Kwinners>0: Kwinners-=1; Kwins+=1

 Nwins=0; Klosers=0; B=B[::-1]
 for i in B:
  if i=='K': Klosers+=1
  elif i=='N' and Klosers>0: Klosers-=1; Nwins+=1

 return (Nwins,len(K)-Kwins)

infile=file('D-large.in','rb+'); outfile=file('D-large.out','wb+')
for casen in range(1,int(infile.readline())+1):
 lenNK=int(infile.readline())
 N=eval('[%s]'%infile.readline().strip().replace(' ',','))
 K=eval('[%s]'%infile.readline().strip().replace(' ',','))
 outfile.write('Case #%i: %i %i\r\n'%((casen,)+answer(N,K)))