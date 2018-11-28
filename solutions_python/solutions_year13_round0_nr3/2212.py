#!/usr/bin/python2

from math import sqrt

#inf = open("fair.in1");
inf = open("C-small-attempt0.in");
#inf = open("C-large.in");

T=int(inf.readline());
for t in xrange(T):
   ls = inf.readline().split();
   a=int(ls[0]);
   b=int(ls[1]);
   count=0;
   for i in xrange(int(sqrt(a-1))+1,int(sqrt(b))+1):
      if str(i) == str(i)[::-1]:
         sq = str(i*i);
         if (sq==sq[::-1]) and (i*i<=b):
            count+=1;
   print "Case #"+str(t+1)+":",count

inf.close();
