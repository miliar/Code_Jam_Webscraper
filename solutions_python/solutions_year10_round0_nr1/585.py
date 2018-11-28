# -*- coding: utf-8 -*-

import os
import sys

def tobin(x, count=30):
        return "".join(map(lambda y:str((x>>y)&1), range(count-1, -1, -1)))


data = open("snap.in","r")

lines =  data.readlines()

cases = int(lines[0].replace('\n',''))

lines = lines[1:]

cases_data = []

for i in range(cases):
  cases_data.append(lines[i].replace('\n','').split())
  cases_data[i][0] = int(cases_data[i][0])
  cases_data[i][1] = int(cases_data[i][1])
  
case_n = 0
output = open("outputsnap.txt","w")

temp = ""
for data in cases_data:
  case_n = case_n+1

  if case_n!=1:
    temp+='\nCase #'+str(case_n)+': '
  else:
    temp+='Case #'+str(case_n)+': '


  n = data[0]
  k = data[1]

  

  mot = ""
  for i in range(n):
    mot+='1'
  nbr = int(mot,2)

  motbin = tobin(k,n)
  if motbin == mot:
    temp+="ON"
  else:
    temp+="OFF"
  

output.write(temp)
output.close()
  


