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

def getTime(src):
   a=src.split(":")
   return int(a[0])*60+int(a[1])

if __name__=='__main__':
   src=sys.argv[1]
   tgt=sys.argv[2]
   infile=open(src,"r")
   outfile=open(tgt,"w")
   linecnt = int(infile.readline())
   for i in range(linecnt):
      latency=int(infile.readline())
      [acnt,bcnt] = infile.readline().split()
      froma = []
      fromb = []
      for j in range(int(acnt)):
         froma.append(map(getTime,infile.readline().split()))
      for j in range(int(bcnt)):
         fromb.append(map(getTime,infile.readline().split()))
      result = getCount(latency,froma,fromb)
      outfile.write("Case #%d: %d %d\n"%(i+1,result[0],result[1]))
#      print "="*10
   infile.close()
   outfile.close()
