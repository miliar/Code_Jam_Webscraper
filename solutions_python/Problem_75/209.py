#!/usr/bin/python

import sys

def solveCase(combines,destroys,test):
  out = [test[0]]
  for i in test[1:]:
    if out and out[-1]+i in combines:
      out[-1] = combines[out[-1]+i]
    elif out and i+out[-1] in combines:
      out[-1] = combines[i+out[-1]]
    else:
      out.append(i)
      for d in destroys:
        if d[0] in out and d[1] in out:
          out = []
  return out

n=0
for row in sys.stdin:
  if n: # Skip first row that is just a count
    rowArray = row.split(' ')
    combineLength = int(rowArray[0])
    combines = rowArray[1:1+combineLength]
    destroyLength = int(rowArray[combineLength+1])
    destroys = rowArray[combineLength+2:combineLength+destroyLength+3]
    test = rowArray[-1].strip()

    combines = dict(((i[0:2],i[2]) for i in combines))
    
    #print combineLength,destroys,test
    print ("Case #%s: %s" % (n,solveCase(combines,destroys,test))).replace("'","")
  n=n+1

