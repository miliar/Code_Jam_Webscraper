#!/usr/bin/python

def solve(n,s,p,tots):
   count =0;
   for it in tots:
      k = it%3;
      if k==0:
         x = it/3;
      elif k==1:
         x = (it+2)/3;
      else:
         x = (it+1)/3;
      if x>=p:
         count+=1;
      elif s>0 and it>1:
         if (k==0 or k==2) and x+1>=p:
            s-=1;
            count+=1;
   return count;

#inF=open("B-small-attempt0.in");
#outF=open("B-small-attempt0.out","w");
inF=open("B-large.in");
outF=open("B-large.out","w");
TC=int(inF.readline());
for tc in xrange(TC):
   ls=inF.readline().split();
   n=int(ls[0]);
   s=int(ls[1]);
   p=int(ls[2]);
   tots = [int(it) for it in ls[3:3+n]];
   outF.write("Case #"+str(tc+1)+": "+str(solve(n,s,p,tots))+"\n");

inF.close();
outF.close();
