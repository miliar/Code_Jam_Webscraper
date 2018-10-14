#!/usr/bin/python

def solve(a,b):
   count = 0;
   sa=str(a);
   sb=str(b);
   lr=range(len(sa));
   for i in xrange(a,b+1):
      si=str(i);
      sj=si;
      pos = set();
      for j in lr:
         sj=sj[1:]+sj[0];
         if sj>si and sj<=sb:
            pos.add(sj);
      count+=len(pos);
   return count;


#inF=open("C-small-attempt0.in");
#outF=open("C-small-attempt0.out","w");
inF=open("C-large.in");
outF=open("C-large.out","w");
TC=int(inF.readline());
for tc in xrange(TC):
   ls=inF.readline().split();
   a=int(ls[0]);
   b=int(ls[1]);
   outF.write("Case #"+str(tc+1)+": "+str(solve(a,b))+"\n");

inF.close();
outF.close();
