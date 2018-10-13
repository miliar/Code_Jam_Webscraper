# -*- coding: utf-8 -*-

infile=open('B-large.in')
outfile=open('B-large.out','w')
T=int(infile.readline().strip())

for case in range(1,T+1):
    
    tis=infile.readline().strip().split(' ')
    N,S,p=tis[0:3]
    N=int(N)
    S=int(S)
    p=int(p)
    tis=tis[3:]
    sum=0
   
    for tii in tis:
       
        ti=int(tii)
        if ti<3*p-4:continue
        if  p==1:
            if ti<1:continue
        if ti>=3*p-2:
            sum=sum+1;continue
        if S>0:
            sum=sum+1
            S=S-1
  
    outfile.write('Case #%i: %d\n'%(case,sum))
    
infile.close()
outfile.close()
print 'ok'

    

