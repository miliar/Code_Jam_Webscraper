#!/usr/bin/env python

import os, numpy, math, sys, string




#========================================================
def return_int(s):
  l = 0
  for i in range(len(s)):
    l+=int(s[i])*(math.pow(10,len(s)-i-1))
  return(int(l))
  
def return_list(i):
  finishFlag = False
  s=[]
  z=10
  while(i>0):
    s.insert(0,i%10)
    i=int(i/10)
  return s
  
def plus_ein(s):
  finishFlag = False
  i = len(s)
  while(not(finishFlag)):
    z = int(s[i-1])
    z += 1
    if (z==10):
      s[i-1]=str(0)
      if ((i-1)==0):
        finishFlag = True
      i-=1
    else:
      s[i-1]=str(z)
      finishFlag = True
  return s

def schieb(s, i=1):
  if i>=len(s):
    return False
  return s[i:]+s[:-(len(s)-i)]
#========================================================


infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])

output = ''


for t in range(T):
  line=lines[1+t].strip().split()
  A = int(line[0])
  B = int(line[1])
  i_list=list(line[0])
  
  i_temp=A
  numRecycl = 0
  res=[]
  while (i_temp<=B):
    #Schieb====================
    for i in range(1,len(i_list)):
      temp_schieben_list=schieb(i_list,i)
      if temp_schieben_list[0]<>'0':
        m = return_int(temp_schieben_list)
        if (i_temp<m) and (m<=B) and (i_temp>=A):
          if (res.count(i_list+temp_schieben_list)==0):
            res.append(i_list+temp_schieben_list)
            numRecycl+=1
          #print "%d %d" %(i_temp, m)
    #Schieb====================
    i_list = plus_ein(i_list)
    i_temp += 1
  
  output += 'Case #%d: %s\n' % (t+1, numRecycl)


print output
file(sys.argv[1]+'.res','w').write(output)
