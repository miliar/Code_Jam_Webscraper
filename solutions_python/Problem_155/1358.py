#!/usr/bin/python

import sys
fname="input"

with open(fname) as f:
    content = f.readlines()
numCase =  int(content[0])

i=1
while i <= numCase:
  res = 0
  j=0
  people = 0
  current = content[i]
  col = current.split(" ")
  while j <= int(col[0]):
    while people < j:
      res += 1
      people += 1
    people +=  int(col[1][j])
    j+=1

  print "Case #"+str(i)+" "+str(res)
  i += 1

