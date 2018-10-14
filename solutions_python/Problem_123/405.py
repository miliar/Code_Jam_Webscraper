#!/usr/bin/python2

from math import sqrt

#inf = open("mote.in1");
#inf = open("A-small-attempt1.in");
inf = open("A-large.in");

sizes = [];

def numOps(a, i, n):
   global sizes;
   if a==1: return n;
   if a>sizes[n-1]: return 0;
   while i<n and a>sizes[i] and a<=sizes[n-1]:
      a+=sizes[i];
      i+=1;
   if a>sizes[n-1]: return 0;
   x=0;
   while a<=sizes[i]:
      a=a*2-1;
      x+=1;
   return min(n-i, x+numOps(a, i, n));


T=int(inf.readline());
for t in xrange(T):
   ls = inf.readline().split();
   a=int(ls[0]);
   n=int(ls[1]);
   sizeS = inf.readline().split();
   sizes = [int(it) for it in sizeS[:n]];
   sizes.sort();
   print "Case #"+str(t+1)+":",numOps(a, 0, n);

inf.close();
