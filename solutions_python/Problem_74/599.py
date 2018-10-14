import string
from math import *
t=int(raw_input(''))

for i in xrange(1,t+1):
  s=0
  a=string.split(raw_input(''))
  n=int(a[0])
  for j in range(2,n*2+1,2):
    a[j]=int(a[j])
  
  o=1
  b=1
  if a[1]=='O':
    o=a[2]
  else:
    b=a[2]
    
  j=3
  w=a[2]
  t=a[2]
  
  while j<n*2:
    if a[j]==a[j-2]:
      w=w+abs(a[j+1]-a[j-1])+1
      t=t+abs(a[j+1]-a[j-1])+1
      if a[j]=='O':
        o=a[j+1]
      else:
        b=a[j+1]
    else:
      if a[j]=='O':
        if abs(o-a[j+1])<=w:
          w=1
          t=t+1
        else:
          t=t+abs(o-a[j+1])-w+1
          w=abs(o-a[j+1])-w+1
        o=a[j+1]
      else:
        if abs(b-a[j+1])<=w:
          w=1
          t=t+1
        else:
          t=t+abs(b-a[j+1])-w+1
          w=abs(b-a[j+1])-w+1
        b=a[j+1]    
    j=j+2
    
  print 'Case #'+str(i)+': '+str(t)
      
  
	
   
