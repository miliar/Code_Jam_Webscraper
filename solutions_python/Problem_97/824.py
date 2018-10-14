#!/usr/bin/python
import sys
data=[[1,9],[10,40],[100,500],[1111,2222]]

if len(sys.argv)>1:
  infi = sys.argv[1]
  data = []
  fi = open(infi)
  lines = fi.readlines()
  d = 0
  for line in lines:
    #print line,len(li)
    if d!=0:
      dataline = line.split(" ")
      data.append([int(dataline[0]),int(dataline[1])])
    d+=1
c = 1
for item in data:
  low = item[0]
  maxx = item[1]
  output =[]
  for i in range(low,maxx+1):
    sti = str(i)
    for sep in range(len(sti)-1):
      data1=int(sti)
      data2=int(sti[sep+1:len(sti)]+sti[0:sep+1])
      maxdata = max(data1,data2)
      mindata = min(data1,data2)
      if(maxdata<=maxx and mindata>=low and mindata<maxdata):
        key = str(min(data1,data2))+str(max(data1,data2))
        if not key in output:
          output.append(key)
  print "Case #"+str(c)+": "+str(len(output))
  c+=1
