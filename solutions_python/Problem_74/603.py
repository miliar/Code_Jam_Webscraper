#!/usr/bin/python2
from sys import stdin



C = int(stdin.readline())
for c in range(1,C+1):
  t = map(str,stdin.readline().split())
  t.pop(0)

  time=0
  pos={}
  pos['O']=1
  pos['B']=1
  goal={}
  


  while(len(t)>0):
    first=t[0]
    goal['O']=-1
    for x in range(0,len(t),2):
      if(t[x]=='O'):
        goal['O']=int(t[x+1])
        break
    goal['B']=-1
    for x in range(0,len(t),2):
      if(t[x]=='B'):
        goal['B']=int(t[x+1])
        break
    #print "goal ",
    #print goal
    

    if(pos[first]<goal[first]):
      pos[first]+=1
      time+=1
    elif(pos[first]>goal[first]):
      pos[first]-=1
      time+=1
    else:
      t.pop(0)
      t.pop(0)
      time+=1

    if(first=='O'): second= 'B'
    else: second= 'O'
    if(goal[second]!=-1):
      if(pos[second]<goal[second]):
        pos[second]+=1
      elif(pos[second]>goal[second]):
        pos[second]-=1
  print "Case #%d: %d" %(c,time)
  
  
  
  
