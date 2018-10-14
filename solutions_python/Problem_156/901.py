#!/usr/bin/python

import sys

def removeMax9(list):
  maxi = max(list)
  if maxi == 9:
    list.remove(maxi)
    list.append(6)
    list.append(3)
  return list

def removeMax(list):
  maxi = max(list)
  if maxi % 2 == 0:
    list.remove(maxi)
    list.append(maxi / 2)
    list.append(maxi / 2)
  else:
    list = [ 0 if (el - 1) <=0 else el - 1 for el in list] 
  return list


def getR(list):
  maxi = max(list)
  if maxi == 1:
    minute = 1
  elif maxi == 9:
    minute = min(min(maxi,1+getR(removeMax(list))),1+getR(removeMax9(list)))
  else:
    minute = min(maxi,1+getR(removeMax(list)))
  return minute


fname=sys.argv[1]

with open(fname) as f:
  content = f.readlines()
numCase =  int(content[0])

i=0
while i < numCase:
  list = []
  j=0
  numberPlates = int(content[2*i+1])
  contenu =  content[2*i+2]
  col = contenu.split(" ")
  while j < numberPlates:
    list.append(int(col[j]))
    j +=1
  minute = getR(list)
  i+=1
  print "Case #"+str(i)+": "+str(minute)
