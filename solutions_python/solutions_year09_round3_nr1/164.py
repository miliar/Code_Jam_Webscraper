#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)<2:
  print "gimme data..."
  sys.exit(1)

def log(s, screen=True):
  if screen:
    print s
  outf.write(s+"\n")

def convert(number,base):
  if base==10:
    return map(int,list(str(number)))
  if number<base:
    return [number]
  c=0
  u=base**c
  while u<=number:
    u*=base
    c+=1
  c-=1
  result=[]
  while c>-1:
    a=number//(base**c)
    b=number%(base**c)
    #print number,base**c,a,b
    if a<>0:
      result.append(a)
    else:
      result.append(b)
    number-=a*(base**c)
    c-=1
  return result

inf_name=sys.argv[1]
outf_name=inf_name[:-2]+'out'
inf=open(inf_name,'r')
outf=open(outf_name,'w')
N=int(inf.next().split()[0])
C=1
for i in xrange(N):
  s=inf.next().split()[0]
  dic={}
  if len(s)>1:
    dic[s[0]]=1
    nums=list(xrange(100))
    nums.pop(1)
    c=0
    for j in s[1:]:
      if j not in dic.keys():
	dic[j]=nums[c]
	c+=1
    w=[dic[j] for j in s]
    base= len(dic)
    if base==1:
      base=2
    value=[ w[len(w)-1-j]*base**j for j in xrange(len(w)-1,-1,-1)]
    #print value
    sv=sum(value)
    print s,w, value, sv
  else:
    sv=1
    print s,"hhhhhhh"
  log("Case #%i: %s" % (C,sv))
  C+=1
outf.close()
inf.close()