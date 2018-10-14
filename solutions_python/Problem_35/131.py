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

print "THIS NIGHT IS A PUNISHMENT\nTHAT'S WHY IT'S SO UGLYYy\n"

def get(x,y):
  if ((x<0 or x>(W-1)) or (y<0 or y>H-1)):
    #print "paff"
    return (1000000,x,y,[0])
  else:	
    return emaps[(x,y)]


def run(field,rcolor):
  while field[3][0]==0:
    cheight,cx,cy,cc=field
    #print "F2: ",field,cx,cy
    cN=get(cx,cy-1)
    cW=get(cx-1,cy)
    cE=get(cx+1,cy)
    cS=get(cx,cy+1)
    nb=[(cN[0],0,cN),(cW[0],1,cW),(cE[0],2,cE),(cS[0],3,cS)] #N,W,E,S 
    nb.sort(reverse=True)
    #print "NB: ",nb
    aha=nb.pop()[2]
    #print "T: ",aha
    theight,tx,ty,tc=target=aha
    #print target, field
    field[3]=rcolor
    if target[0]<field[0]:
      field=target
      continue
    else:
      break
  return field[3][0]


def printit2():
  #print emaps
  for i in xrange(H):
      s=''
      for j in xrange(W):
	s+=str(get(j,i)[0])+' '
	#s+=str(chr(97+get(j,i)[3]]]))+' '
      print s
  print "\n"
  for i in xrange(H):
      s=''
      for j in xrange(W):
	#print get(j,i)
	s+=str(chr(96+get(j,i)[3][0]))+' '
      print s
  print "\n"
  
def printit():
  #print emaps
  for i in xrange(H):
    s=''
    for j in xrange(W):
      #print get(j,i)
      s+=str(chr(96+get(j,i)[3][0]))+' '
    outf.write(s+"\n")

T=int(inf.next().split()[0])
values=[]
for C in xrange(1,T+1):
  H,W=[int(x) for x in inf.next().split()]
  emaps={}
  values=[]
  colors={}
  groups={0:0}
  color=1
  group=1
  zero=[0]
  for j in xrange(H):
    line=[int(x) for x in inf.next().split()]
    for k in xrange(W):
      a=[line[k],k,j,[0]]
      emaps[(k,j)]=a
  print "Case #"+str(C)+": "
  outf.write("Case #"+str(C)+":\n")
  if 1:
    for m in xrange(H):
     for n in xrange(W):
      #print n,m
      field=get(n,m)
      #print "F: ",field
      if field[3][0]<>0:
	continue
      rcolor=[color]
      newcolor=run(field,rcolor)
      if newcolor<>color:
	rcolor[0]=newcolor
      else:
	color+=1
      #for oo in xrange(H):
      # s=''
      # for pp in xrange(W):
      #  s+=str(emaps[(pp,oo)][3])
      # print s
      #printit2()
    printit()
outf.close()
inf.close()
