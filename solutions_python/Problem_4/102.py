#!/usr/bin/python
import sys
import time
import re


def getCount(latency,fa,fb):
   a=0
   b=0
   c=0
   froma=fa[:]
   fromb=fb[:]
   for i in fb:
      froma.append([i[1]+latency,-1])
   froma.sort()
#   while len(froma) and froma[-1][1]==-1 : froma=froma[:-1]
   for i in froma:
      if i[1]>0 :
         if c> 0: c-=1
	 else : a+=1
      else : c+=1

   c=0
   for i in fa:
      fromb.append([i[1]+latency,-1])
   fromb.sort()
#   while len(fromb) and fromb[-1][1]==-1 : fromb=fromb[:-1]
   for i in fromb:
      if i[1]>0 : 
	 if c>0 : c-=1
         else : b+=1
      else : c+=1

#   for i in froma:
#      print i
#   print "-"*10
#   for i in fromb:
#      print i

   return (a,b)


if __name__=='__main__':
   src=sys.argv[1]
   tgt=sys.argv[2]
   infile=open(src,"r")
   outfile=open(tgt,"w")
   casecnt = int(infile.readline())
   for i in range(casecnt):
      size=int(infile.readline())
      a = map(int,infile.readline().split())
      b = map(int,infile.readline().split())
      a.sort()
      b.sort(reverse=True)
      c=0
      for j in range(size) : c+=a[j]*b[j]
      outfile.write("Case #%d: %d\n"%(i+1,c))
   infile.close()
   outfile.close()
