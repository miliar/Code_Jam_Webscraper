#!/usr/bin/env python
import sys

def searchNcount(sstr, string, pos1, pos2):
  global pcounts
  if(pos1 == len(sstr)): 
    return 1
  else:
    if(pos2 == len(string)):
      return 0
  if(pcounts.has_key((pos1,pos2))):
    return pcounts[(pos1,pos2)]
  i = pos2
  mycount = 0
  while(i < len(string)):
    if(sstr[pos1] == string[i]):
      mycount += searchNcount(sstr, string, pos1+1, i+1)
    i += 1
  pcounts[(pos1,pos2)] = mycount % 10000
  return mycount
  

global pcounts
pcounts = {}
count = raw_input()
N = eval(count)
sstr = "welcome to code jam"
wcount = 0
for i in range(N):
  pcounts = {}
  string = raw_input()
  searchNcount(sstr, string, 0, 0)
  print "Case #%d: %04d" % (i+1,pcounts[(0,0)] % 10000)