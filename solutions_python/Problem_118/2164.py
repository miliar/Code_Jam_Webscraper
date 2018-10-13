#!/usr/bin/python
import sys
import math
import operator
from operator import itemgetter
data = [[1,4],[10,120],[100,1000],[10,121]]
if len(sys.argv)>1:
  infi = sys.argv[1]
  data = []
  fi = open(infi)
  lines = fi.readlines()
  d = 0
  for line in lines:
    if len(line)<2:
      continue
    strtmp = line.replace("\n","")
    if d!=0:
      dataline = strtmp.split(" ")
      data.append(map(int,dataline))
    d+=1
c = 0
while c < len(data):
 datan = data[c]
 count = 0
 mind = int(math.ceil(math.sqrt(int(datan[0]))))
 maxd = int(math.floor(math.sqrt(int(datan[1]))))+1
 for n in xrange(mind,maxd):
   if  str(n)[::-1]==str(n):
     m = str(n*n)
     if m[::-1]==m:
       count+=1
   else:
     continue
 print "Case #"+str(c+1)+": "+str(count)
 c+=1
