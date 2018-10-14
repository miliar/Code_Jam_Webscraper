#!/usr/bin/env python

f=open('C-small-attempt0.in','r')
f1=open('output2.txt','w')
n=int(f.readline())
for j in xrange(1,n+1):
   line=f.readline().split()
   end=int(line[1])
   count=0
   num=line[0]
   size=len(num)
   last=()
   while int(num)<end:
      if size<=1:
         break
      else:
         for i in xrange(1,size):
            numc=num[-i:]+num[:-i]
            if numc[0] !='0' and numc > num and int(numc)<=end and last != (num,numc):
               count+=1
               last=(num,numc)
      num=str(int(num)+1)
   f1.write("Case #%d: %d\n"%(j,count))
      
f1.close()

f.close()


