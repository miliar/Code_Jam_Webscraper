#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)<2:
  print "give me data..."
  sys.exit(1)

inf_name=sys.argv[1]
outf_name=inf_name[:-2]+'out'
inf=open(inf_name,'r')
outf=open(outf_name,'w')

words=[]
L,D,N=[int(x) for x in inf.next().split()]

for i in xrange(D):
  word=inf.next()[:-1]
  print "w: ",word
  words.append(word)
for C in xrange(1,N+1):
  w=0
  line=inf.next()[:-1]
  fck=[]
  for x in line.split(')'):
    if '(' in x:
      h,t=x.split('(')
      hx=list(h)
      hx.append(t)
    else:
      hx=list(x)
    fck.extend(hx)
  
  if len(fck)<>L:
    print "FUCK.",C
    sys.exit(0)
  w=len(words)
  for i in xrange(len(words)):
    for j in xrange(len(words[i])):
      if words[i][j] in fck[j]:
	continue
      else:	
	w-=1
	break
  print "Case #"+str(C)+": "+str(w)
  #print line
  #print fck,"\n"

  outf.write("Case #"+str(C)+": "+str(w)+'\n')
  C+=1
  
outf.close()
inf.close()
