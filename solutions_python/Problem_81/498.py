#!/usr/bin/python2
from sys import stdin



C = int(stdin.readline())

for c in range(1,C+1):
  g=[]
  print "Case #%d:" %c
  t = int(stdin.readline())
  for te in range(0,t):#wp
    g.append([])
    games=stdin.readline()[:-1]
    i=0.0
    n=0
    g[te].append(games)
    for a in games:
      if(a=="1" or a=="0"):
        i+=int(a)
        n+=1
    i/=n
    g[te].append(n)
    g[te].append(i)

  #owp
  for te in range(0,t):
    i=0.0
    n=0
    for q,a in enumerate(g[te][0]):
      #print "AQ",a,q
      if(a=="1"):
        n+=1
        i+=(g[q][2]*g[q][1])/(g[q][1]-1)
      elif(a=="0"):
        n+=1
        i+=(g[q][2]*g[q][1]-1.0)/(g[q][1]-1)
        #print (g[q][2]*g[q][1]-1.0)/(g[q][1]-1)
    i/=n
    g[te].append(i)

  #oowp
  for te in range(0,t):
    i=0.0
    n=0
    for q,a in enumerate(g[te][0]):
      #print "AQ",a,q
      if(a=="1" or a=="0"):
        n+=1
        i+=g[q][3]
    i/=n
    g[te].append(i)
  #print g
  for a in g:
    print 0.25 * a[2] + 0.50 * a[3] + 0.25 * a[4]
    
