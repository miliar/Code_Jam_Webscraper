#!/usr/bin/python
import sys
import time
import re


def getCount(ss,qs):
   cnt=0
   ls=ss[:]
   for i in qs:
      if i in ls:
         ls.remove(i)
         if len(ls)==0 :
            cnt+=1
            ls=ss[:]
	    ls.remove(i)

   return cnt


if __name__=='__main__':
   src=sys.argv[1]
   tgt=sys.argv[2]
   infile=open(src,"r")
   outfile=open(tgt,"w")
   cnt = int(infile.readline())
   for i in range(cnt):
      ss=[]
      qs=[]
      s=int(infile.readline())
      for j in range(s):
         ss.append(infile.readline())
      q=int(infile.readline())
      for j in range(q):
         qs.append(infile.readline())
      result = getCount(ss,qs)
      outfile.write("Case #%d: %d\n"%(i+1,result))
#      print "="*10
   infile.close()
   outfile.close()
