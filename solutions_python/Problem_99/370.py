#!/usr/bin/python
import sys
import operator
from operator import itemgetter
data = [[2,5],[0.6,0.6],[1,20],[1],[3,4],[1,0.9,0.1]]
if len(sys.argv)>1:
  infi = sys.argv[1]
  data = []
  fi = open(infi)
  lines = fi.readlines()
  d = 0
  for line in lines:
    #print line,len(li)
    strtmp = line.replace("\n","")
    if d!=0:
      dataline = strtmp.split(" ")
      data.append(map(float,dataline))
    d+=1
c = 1
for i in range(0,len(data),2):
  typeNow = data[i][0]
  allChar = data[i][1]
  prob = data[i+1]
  newTypeCount = allChar+1
  expected = []
  for numdelete in range(typeNow):
    propOther = reduce(lambda x,y:x*y,prob[0:len(prob)-numdelete])
    propPrefixHasFalse = 1-propOther
    dataPrefixTrue = numdelete+(allChar-typeNow+numdelete)+1
    dataPrefixFalse = dataPrefixTrue + allChar+1  
    expected.append(dataPrefixTrue*propOther+propPrefixHasFalse*dataPrefixFalse)
  expected.append(allChar+2)
  print "Case #"+str(i/2+1)+":",
  print ("%.6f" % min(expected))
