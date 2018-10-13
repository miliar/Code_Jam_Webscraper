#!/usr/bin/python2
from sys import stdin



C = int(stdin.readline())
for case in range(1,C+1):
  q,t = str,stdin.readline().split()
  #print t
  comb={}
  opp={}
  c=int(t[0]) #combine rules
  t.pop(0)
  for x in range(0,c):
    if(not t[0][0] in comb):
      comb[t[0][0]]={}
    if(not t[0][1] in comb):
      comb[t[0][1]]={}
    comb[t[0][0]][t[0][1]]=t[0][2]
    comb[t[0][1]][t[0][0]]=t[0][2]
    t.pop(0)


  c=int(t[0]) #oppose rules
  t.pop(0)
  for x in range(0,c):
    if(not t[0][0] in opp):
      opp[t[0][0]]={}
    opp[t[0][0]][t[0][1]]=True
    t.pop(0)

  inv=[]
  #if(case>5): break
  for a in range(0,len(t[1])):
    inv.append(t[1][a])
    
  for l in range(0,len(inv)+1):
    if(l>1 and inv[l-2] in comb and inv[l-1] in comb[inv[l-2]]):
      inv[l-2]=comb[inv[l-2]][inv[l-1]]
      inv[l-1]=''
    if(l>1 and inv[l-1] in comb and inv[l-2] in comb[inv[l-1]]):
      inv[l-2]=comb[inv[l-1]][inv[l-2]]
      inv[l-1]=''
    for a in range(0,l-1):
      for b in range(a+1,l):
        
          #oppose
        if((inv[a] in opp and inv[b] in opp[inv[a]]) or
           (inv[b] in opp and inv[a] in opp[inv[b]])):
          for q in range(0,b+1):
            inv[q]=''
            #print "opp",inv

  for q in range(len(inv)-1,-1,-1):
    if(inv[q]==''): inv.pop(q)
  out= "Case #%d: [" % case
  for a in range(0,len(inv)):
    out+= str(inv[a])
    if(a<len(inv)-1):
      out+=", "
  out+="]"
  print out
  
